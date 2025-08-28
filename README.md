# Atividade-pr-tica-POO-Observer-
Atividade Prática – Padrão Observer (POO II)  Este repositório contém a implementação prática do padrão de projeto Observer, desenvolvido como parte da disciplina Programação Orientada a Objetos II. A atividade foi dividida em duas partes, cada uma demonstrando o uso do Observer em contextos diferentes.

📌 Parte 1 – Operações Matemáticas

Implementação de um sujeito concreto que mantém dois valores inteiros.
Sempre que os valores são atualizados, os observadores registrados são notificados automaticamente e realizam diferentes operações:

DivObserver → divisão inteira

ModObserver → resto da divisão (módulo)

MultObserver → multiplicação

O objetivo é mostrar como o Observer permite desacoplar a lógica de atualização dos cálculos da lógica principal.

📌 Parte 2 – Agência de Notícias (Reuters)

Simulação de uma agência de notícias (Reuters) que notifica seus canais de TV assinantes quando uma nova notícia de última hora é publicada.

A agência funciona como sujeito (observable).

Os canais de TV funcionam como observadores (observers).

Ao publicar uma notícia, todos os canais inscritos são notificados instantaneamente.

Este exemplo reforça o uso do padrão em um cenário mais próximo de aplicações do mundo real.

🚀 Tecnologias Utilizadas

Python 3

Padrão de Projeto Observer (GoF)

🎯 Objetivo da Atividade

Exercitar os conceitos de desacoplamento e programação orientada a interfaces.

Demonstrar a aplicação prática do padrão Observer em diferentes domínios (matemática e comunicação).
