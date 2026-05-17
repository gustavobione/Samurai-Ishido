using UnityEngine;

public class CameraFollow : MonoBehaviour
{
    [Header("Alvo")]
    public Transform target;

    [Header("Suavização")]
    public float smoothSpeed = 5f;

    [Header("Offset")]
    public Vector2 offset = new Vector2(2f, 1f); // lead na direção do movimento

    [Header("Limites da câmera")]
    public bool useBounds = false;
    public Vector2 minBounds;
    public Vector2 maxBounds;

    [Header("Deadzone")]
    public float deadzoneX = 0.5f;
    public float deadzoneY = 0.3f;

    private PlayerController playerController;
    private Vector3 velocity = Vector3.zero;
    private Vector3 targetPosition;

    void Start()
    {
        if (target != null)
            playerController = target.GetComponent<PlayerController>();

        // Começa na posição do alvo sem suavização
        transform.position = GetTargetPosition();
    }

    void LateUpdate()
    {
        if (target == null) return;

        targetPosition = GetTargetPosition();

        // Aplica deadzone — câmera só move se o player sair da zone
        float distX = Mathf.Abs(transform.position.x - targetPosition.x);
        float distY = Mathf.Abs(transform.position.y - targetPosition.y);

        Vector3 desiredPos = transform.position;

        if (distX > deadzoneX)
            desiredPos.x = targetPosition.x;
        if (distY > deadzoneY)
            desiredPos.y = targetPosition.y;

        // Suaviza o movimento
        transform.position = Vector3.SmoothDamp(
            transform.position,
            desiredPos,
            ref velocity,
            1f / smoothSpeed
        );

        // Aplica limites se configurado
        if (useBounds)
        {
            transform.position = new Vector3(
                Mathf.Clamp(transform.position.x, minBounds.x, maxBounds.x),
                Mathf.Clamp(transform.position.y, minBounds.y, maxBounds.y),
                transform.position.z
            );
        }
    }

    Vector3 GetTargetPosition()
    {
        Vector3 pos = target.position;

        // Lead na direção do movimento
        if (playerController != null)
            pos.x += offset.x * playerController.FacingDirection;

        pos.y += offset.y;
        pos.z = transform.position.z; // mantém o Z da câmera

        return pos;
    }

    // Chamado pelo GameManager ao respawnar — teleporta sem suavização
    public void SnapToTarget()
    {
        if (target == null) return;
        transform.position = GetTargetPosition();
        velocity = Vector3.zero;
    }
}