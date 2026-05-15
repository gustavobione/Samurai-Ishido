# 🗡️ Samurai Ishido

> **Status do Projeto:** Em Desenvolvimento 🚧
> **Gênero:** Metroidvania 2D (Pixel Art)
> **Motor Gráfico:** Unity 
> **Linguagem:** C#

Um jogo de plataforma e ação no estilo Metroidvania focado em combate preciso, exploração e progressão de habilidades. Acompanhe a jornada do Ishido por cenários como a **Colina Lótus** e a **Floresta Murmurante**, enfrentando Yokais (Kappas, Tengus) até o confronto contra o chefe **Kuroi Shinen**.

---

## 📂 Estrutura do Projeto

Nossa pasta `Assets` está organizada da seguinte forma para garantir que ninguém se perca:

* 📁 **`_Scripts/`** - Todos os códigos em C# (Player, Inimigos, Managers).
* 📁 **`Arte/`** - Spritesheets, cenários, UI e efeitos visuais (VFX).
* 📁 **`Audio/`** - Efeitos sonoros (SFX) e músicas de fundo (BGM).
* 📁 **`Prefabs/`** - Nossos "blocos de montar" (Inimigos, Objetos, Checkpoints).
* 📁 **`Scenes/`** - Fases oficiais e cenas de teste individuais.
* 📁 **`Settings/`** - Configurações do Input System, Física e Renderização (URP).

---

## 🛠️ Guia da Equipe: Como Trabalhar no Projeto

Para evitar que arquivos corrompam (especialmente as *Scenes* do Unity), utilizamos o padrão **Git Flow** aliado a regras rígidas de manipulação de Cenas e Prefabs.

### 1. A Regra de Ouro do Unity (Prefabs > Scenes)
* **Nunca edite a mesma Cena (`.unity`) que outra pessoa ao mesmo tempo.** O Git não consegue mesclar arquivos de cena e o trabalho será perdido.
* **Level Design:** Apenas o Level Designer responsável deve alterar o arquivo da cena principal (ex: montando a Colina Lótus).
* **Arte, Áudio e Código:** Trabalhem dentro de **Prefabs**. Se precisar alterar o comportamento de um inimigo ou o som de um pulo, edite o arquivo `.prefab`. Essas alterações refletirão automaticamente na cena principal sem gerar conflitos.

### 2. O Fluxo de Versionamento (Git Flow)
Nós possuímos duas branches principais:
* `main` ➔ O jogo final, estável e testado.
* `dev` ➔ O nosso "chão de fábrica". **Ninguém programa direto na dev.**

**Passo a Passo do Dia a Dia:**

1. **Puxe as atualizações:** Antes de abrir o Unity, garanta que seu repositório está atualizado.

```bash
   git checkout dev
   git pull origin dev
```
Crie sua Cópia (Branch de Tarefa): Vai fazer o pulo do Ishido? Crie uma branch específica.

```Bash
git checkout -b feature/pulo-ishido
```

Trabalhe e Salve: Fez o trabalho no Unity? Feche o motor, salve e envie.

```Bash
git add .
git commit -m "Feat: Adiciona script de pulo duplo e audio"
git push -u origin feature/pulo-ishido
```

Pull Request (PR): Vá até o GitHub e abra um Pull Request da sua branch para a dev. O Líder Técnico (Gustavo) fará a revisão do código e aprovará a entrada no jogo oficial.

**📥 Como Clonar este Repositório (Para a Equipe)**

Este projeto utiliza Git LFS para suportar arquivos de imagem e áudio pesados. Antes de clonar, certifique-se de ter o Git LFS instalado na sua máquina.

Abra o terminal onde deseja salvar o jogo.

Inicie o LFS na sua máquina:

```Bash
git lfs install
```

Clone o projeto:

```Bash
git clone [[URL_DO_REPOSITORIO_AQUI](https://github.com/gustavobione/Samurai-Ishido.git)]
```

Abra o Unity Hub > Clique em Add > Selecione a pasta clonada. O Unity baixará todos os pacotes automaticamente na primeira execução (pode demorar alguns minutos).