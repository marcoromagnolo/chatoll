# Chatoll
Chat Frontend for Ollama API

## Install Ollama
* https://ollama.com/download

## Instruction for linux:

```
curl -fsSL https://ollama.com/install.sh | sh
```

Run Ollama with your model: I chose deepseek-r1.
This will download the model and run chat agent.
```
ollama run deepseek-r1:1.5b
```

Create your custom model:
```
FROM deepseek-r1
PARAMETER temperature 0.7
SYSTEM "Sei un scienziato esperto in tutte le materie scientifiche. Fornisci sempre risposte in lingua italiana precise e rigorosamente scientifica."
```

ollama create mymodel -f Modelfile

```
ollama run mymodel
```
