using UnityEngine;

public class PlayerStats : MonoBehaviour
{
    [Header("HP")]
    public float maxHP = 100f;
    public float currentHP;

    [Header("Éter")]
    public float maxEter = 50f;
    public float currentEter;
    public float eterSaturationThreshold = 50f;
    public float eterDrainPerSecond = 5f; // drena quando saturado
    public float hpDrainWhenSaturated = 1f;

    [Header("Estado")]
    public bool isSaturated = false;
    public bool isDead = false;

    // Eventos para a UI escutar
    public System.Action<float, float> OnHPChanged;
    public System.Action<float, float> OnEterChanged;
    public System.Action OnDeath;
    public System.Action OnSaturated;
    public System.Action OnSaturationEnd;

    void Start()
    {
        currentHP = maxHP;
        currentEter = 0f;
    }

    void Update()
    {
        HandleSaturation();
    }

    // ── HP ──────────────────────────────────────────

    public void TakeDamage(float amount)
    {
        if (isDead) return;

        currentHP -= amount;
        currentHP = Mathf.Clamp(currentHP, 0, maxHP);
        OnHPChanged?.Invoke(currentHP, maxHP);

        if (currentHP <= 0)
            Die();
    }

    public void Heal(float amount)
    {
        if (isDead) return;

        currentHP += amount;
        currentHP = Mathf.Clamp(currentHP, 0, maxHP);
        OnHPChanged?.Invoke(currentHP, maxHP);
    }

    void Die()
    {
        isDead = true;
        OnDeath?.Invoke();
    }

    // ── ÉTER ────────────────────────────────────────

    public void AddEter(float amount)
    {
        currentEter += amount;

        // Saturação se passar do máximo
        if (currentEter > maxEter && !isSaturated)
        {
            isSaturated = true;
            OnSaturated?.Invoke();
        }

        // Não tem teto — drena naturalmente via Update
        OnEterChanged?.Invoke(currentEter, maxEter);
    }

    public bool ConsumeEter(float amount)
    {
        if (currentEter < amount) return false;

        currentEter -= amount;
        currentEter = Mathf.Max(0, currentEter);
        OnEterChanged?.Invoke(currentEter, maxEter);
        return true;
    }

    void HandleSaturation()
    {
        if (!isSaturated) return;

        // Drena éter excedente
        currentEter -= eterDrainPerSecond * Time.deltaTime;

        // Drena HP enquanto saturado
        TakeDamage(hpDrainWhenSaturated * Time.deltaTime);

        // Sai da saturação quando voltar ao normal
        if (currentEter <= maxEter)
        {
            currentEter = maxEter;
            isSaturated = false;
            OnSaturationEnd?.Invoke();
        }

        OnEterChanged?.Invoke(currentEter, maxEter);
    }

    // ── UTILITÁRIOS ─────────────────────────────────

    public bool IsHPCritical() => currentHP <= maxHP * 0.3f;
    public bool IsEterEmpty() => currentEter <= 0f;

    public void FullRestore()
    {
        currentHP = maxHP;
        currentEter = 0f;
        isDead = false;
        isSaturated = false;
        OnHPChanged?.Invoke(currentHP, maxHP);
        OnEterChanged?.Invoke(currentEter, maxEter);
    }
}