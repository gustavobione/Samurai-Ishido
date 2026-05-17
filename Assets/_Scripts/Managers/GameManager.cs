using UnityEngine;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{
    public static GameManager Instance { get; private set; }

    [Header("Referências")]
    public PlayerController playerController;
    public PlayerStats playerStats;
    public CameraFollow cameraFollow;

    [Header("Respawn")]
    public Transform lastSanctuaryPosition;
    public float respawnDelay = 2f;

    // Estado do jogo
    public bool IsGamePaused { get; private set; }
    public bool IsPlayerDead { get; private set; }

    void Awake()
    {
        // Singleton
        if (Instance != null && Instance != this)
        {
            Destroy(gameObject);
            return;
        }
        Instance = this;
    }

    void Start()
    {
        if (playerStats != null)
        {
            playerStats.OnDeath += HandlePlayerDeath;
        }

        // Posição inicial de respawn é onde o jogador começa
        if (playerController != null)
            lastSanctuaryPosition = playerController.transform;
    }

    // ── SANTUÁRIO ────────────────────────────────────

    public void RegisterSanctuary(Transform sanctuaryTransform)
    {
        lastSanctuaryPosition = sanctuaryTransform;
        playerStats.FullRestore();
        Debug.Log($"Santuário registrado: {sanctuaryTransform.name}");
    }

    // ── MORTE E RESPAWN ──────────────────────────────

    void HandlePlayerDeath()
    {
        IsPlayerDead = true;
        StartCoroutine(RespawnRoutine());
    }

    System.Collections.IEnumerator RespawnRoutine()
    {
        // Aguarda a animação de morte
        yield return new WaitForSeconds(respawnDelay);

        Respawn();
    }

    void Respawn()
    {
        if (lastSanctuaryPosition == null) return;

        // Move o player para o santuário
        playerController.transform.position = lastSanctuaryPosition.position;

        // Reseta stats
        playerStats.FullRestore();
        IsPlayerDead = false;

        // Teleporta câmera sem suavização
        if (cameraFollow != null)
            cameraFollow.SnapToTarget();

        Debug.Log("Player respawnou no santuário.");
    }

    // ── PAUSE ────────────────────────────────────────

    public void PauseGame()
    {
        IsGamePaused = true;
        Time.timeScale = 0f;
    }

    public void ResumeGame()
    {
        IsGamePaused = false;
        Time.timeScale = 1f;
    }

    // ── CENA ─────────────────────────────────────────

    public void LoadScene(string sceneName)
    {
        Time.timeScale = 1f;
        SceneManager.LoadScene(sceneName);
    }

    public void RestartScene()
    {
        LoadScene(SceneManager.GetActiveScene().name);
    }
}