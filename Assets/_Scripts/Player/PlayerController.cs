using UnityEngine;
using UnityEngine.InputSystem;

[RequireComponent(typeof(Rigidbody2D))]
[RequireComponent(typeof(PlayerStats))]
public class PlayerController : MonoBehaviour
{
    [Header("Movimento")]
    public float speed = 5f;
    public float jumpForce = 10f;

    [Header("Dash")]
    public float dashSpeed = 12f;
    public float dashDuration = 0.3f;
    public float dashCooldown = 0.8f;

    [Header("Ground Check")]
    public Transform groundCheck;
    public float groundCheckRadius = 0.1f;
    public LayerMask groundLayer;

    [Header("Pulo")]
    public float fallMultiplier = 2.5f;    // queda mais pesada
    public float lowJumpMultiplier = 2f;   // pulo curto se soltar cedo

    // Componentes
    private Rigidbody2D rb;
    private PlayerStats stats;

    // Estado
    private bool isGrounded;
    private bool isDashing;
    private bool canDash = true;
    private float dashTimer;
    private float dashCooldownTimer;
    private float dashDirection;

    // Controle de input
    private float moveInput;
    private bool jumpPressed;
    private bool jumpHeld;
    private bool dashPressed;

    // Direção que o personagem está olhando (1 = direita, -1 = esquerda)
    public float FacingDirection { get; private set; } = 1f;

    // Eventos
    public System.Action OnDash;
    public System.Action OnLand;
    public System.Action OnJump;

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        stats = GetComponent<PlayerStats>();
    }

    void Update()
    {
        if (stats.isDead) return;

        GatherInput();
        CheckGround();
        HandleDashCooldown();
    }

    void FixedUpdate()
    {
        if (stats.isDead) return;

        if (isDashing)
        {
            HandleDash();
            return; // durante dash não aplica movimento normal
        }

        HandleMovement();
        HandleJump();
        HandleGravity();
    }

    // ── INPUT ────────────────────────────────────────

    void GatherInput()
    {
        // Movimento
        moveInput = 0f;
        if (Keyboard.current.aKey.isPressed) moveInput = -1f;
        if (Keyboard.current.dKey.isPressed) moveInput = 1f;

        // Pulo
        jumpPressed = Keyboard.current.spaceKey.wasPressedThisFrame ||
                      Keyboard.current.wKey.wasPressedThisFrame;
        jumpHeld = Keyboard.current.spaceKey.isPressed ||
                   Keyboard.current.wKey.isPressed;

        // Dash
        dashPressed = Keyboard.current.leftShiftKey.wasPressedThisFrame;

        // Descer de plataforma
        if ((Keyboard.current.sKey.isPressed || Keyboard.current.downArrowKey.isPressed)
            && jumpPressed)
        {
            TryDropDownPlatform();
        }

        // Iniciar dash
        if (dashPressed && canDash && !isDashing)
        {
            StartDash();
        }
    }

    // ── MOVIMENTO ────────────────────────────────────

    void HandleMovement()
    {
        rb.linearVelocity = new Vector2(moveInput * speed, rb.linearVelocity.y);

        if (moveInput != 0f)
        {
            FacingDirection = Mathf.Sign(moveInput);
            Vector3 currentScale = transform.localScale;
            // Mantém a escala original (ex: 0.4) e só inverte o sinal do X
            currentScale.x = Mathf.Abs(currentScale.x) * FacingDirection;
            transform.localScale = currentScale;
        }
    }

    // ── PULO ─────────────────────────────────────────

    void HandleJump()
    {
        if (jumpPressed && isGrounded)
        {
            rb.linearVelocity = new Vector2(rb.linearVelocity.x, jumpForce);
            OnJump?.Invoke();
        }
    }

    void HandleGravity()
    {
        // Queda mais pesada
        if (rb.linearVelocity.y < 0)
        {
            rb.linearVelocity += Vector2.up * Physics2D.gravity.y
                                * (fallMultiplier - 1) * Time.fixedDeltaTime;
        }
        // Pulo curto se soltar o botão cedo
        else if (rb.linearVelocity.y > 0 && !jumpHeld)
        {
            rb.linearVelocity += Vector2.up * Physics2D.gravity.y
                                * (lowJumpMultiplier - 1) * Time.fixedDeltaTime;
        }
    }

    // ── GROUND CHECK ─────────────────────────────────

    bool wasGrounded = false;

    void CheckGround()
    {
        wasGrounded = isGrounded;
        isGrounded = Physics2D.OverlapCircle(
            groundCheck.position,
            groundCheckRadius,
            groundLayer
        );

        // Evento de aterrissar
        if (!wasGrounded && isGrounded)
            OnLand?.Invoke();
    }

    public bool IsGrounded() => isGrounded;

    // ── DASH ─────────────────────────────────────────

    void StartDash()
    {
        isDashing = true;
        canDash = false;
        dashTimer = dashDuration;

        // Direção do dash — movimento atual ou direção que está olhando
        dashDirection = moveInput != 0 ? Mathf.Sign(moveInput) : FacingDirection;

        OnDash?.Invoke();
    }

    void HandleDash()
    {
        dashTimer -= Time.fixedDeltaTime;

        rb.linearVelocity = new Vector2(dashDirection * dashSpeed, 0f);

        if (dashTimer <= 0f)
        {
            isDashing = false;
            rb.linearVelocity = new Vector2(0f, rb.linearVelocity.y);
            dashCooldownTimer = dashCooldown;
        }
    }

    void HandleDashCooldown()
    {
        if (!canDash)
        {
            dashCooldownTimer -= Time.deltaTime;
            if (dashCooldownTimer <= 0f)
                canDash = true;
        }
    }

    public bool IsDashing() => isDashing;

    // ── PLATAFORMA ONE-WAY ───────────────────────────

    void TryDropDownPlatform()
    {
        // Desativa colisão com plataforma one-way temporariamente
        // Funciona com o componente PlatformEffector2D do Unity
        Collider2D col = GetComponent<Collider2D>();
        if (col != null)
            StartCoroutine(DisablePlatformCollision(col));
    }

    System.Collections.IEnumerator DisablePlatformCollision(Collider2D col)
    {
        Physics2D.IgnoreLayerCollision(
            gameObject.layer,
            LayerMask.NameToLayer("OneWayPlatform"),
            true
        );
        yield return new WaitForSeconds(0.3f);
        Physics2D.IgnoreLayerCollision(
            gameObject.layer,
            LayerMask.NameToLayer("OneWayPlatform"),
            false
        );
    }

    // ── DEBUG ────────────────────────────────────────

    void OnDrawGizmosSelected()
    {
        if (groundCheck == null) return;
        Gizmos.color = isGrounded ? Color.green : Color.red;
        Gizmos.DrawWireSphere(groundCheck.position, groundCheckRadius);
    }
}