using UnityEngine;
using UnityEngine.SceneManagement;

public class MenuManager : MonoBehaviour
{
    public void IniciarJogo()
    {
        // Vai carregar a cena do jogo (precisamos colocar o nome exato dela)
        SceneManager.LoadScene("01_Gameplay"); 
    }
}