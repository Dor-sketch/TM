# Introduction to the Theory of Computation and Complexity (20585): MMN12

Dor Pascal, 2024(a)

---

- [Question 1](#question-1)
  - [1.1](#11)
  - [1.2](#12)
- [Question 2](#question-2)
  - [2.1](#21)
  - [2.2](#22)
  - [2.3](#23)
- [Question 3](#question-3)
- [Question 4](#question-4)
- [Question 5](#question-5)
  - [5.1](#51)
  - [5.2](#52)
  - [5.3](#53)

---

## Question 1

### 1.1

$M$ dosn not decide any language, because it does not reject any input. According to the definition of a langugae that is decided by a TM, TM must be a decider - a TM that `always make a decision to accept or reject. A decider that regonize some langugae also is said to decide that langugae.` (Sipser, 2006, p. 170) So in the case of non-decider TM, it does not decide any language, thus the language $L$ that $M$ decides is _not existing_, or $L(M) = \emptyset$.

**Question:** Can we talk about a language that is decided by a TM that is not a decider? Formally, I thoght the `decide` is a property of only decider TM.

### 1.2

$M$ accepts the languguage of string such that each string represent encoding of a context free grammar that generates at least one word. Formally, $L(M) = \{⟨G⟩ | G \ is \ a \ CFG \ and \ L(G) \neq \emptyset \}$. This is because $M$ accepts the encoding of G, only if there is word $w$ such that $⟨G,w⟩\in  A_{CFG}$, and according to the definition of $A_{CFG}$ from p. 198,  $⟨G,w⟩\in  A_{CFG}$ if and only if $w\in L(G)$, so $M$ accepts $⟨G⟩$ if and only if $L(G) \neq \emptyset$.

## Question 2

### 2.1

If we change the proof of `THEROM 4.11` such that $D$ will run $H$ on input $⟨M,⟨M⟩^R⟩$, then we **wont** get a contradiction. On input $⟨D⟩$ $D$ will run $H$ on input $⟨D,⟨D⟩^R⟩$.

We will break the options for $D(⟨D⟩)$:

---

If $H$ **does not accept** $⟨D,⟨D⟩^R⟩$:

it means $D$ **does not accept**  $\boldsymbol{⟨D⟩^R}$, and thus $D$ **does** accepts  $\boldsymbol{⟨D⟩}$, wich is not a contradiction because there might be some TM $D$ such that if we run $H$ on $⟨D,⟨D⟩⟩$, then $H$ will accept but if we run $H$ on $⟨D,⟨D⟩^R⟩$, then $H$ will reject.

---

If $H$ accepts $⟨D,⟨D⟩^R⟩$:

it means $D$ accepts  $\boldsymbol{⟨D⟩^R}$, and thus $D$ rejects  $\boldsymbol{⟨D⟩}$. Again no contradiction here because there might be some TM $D$ such that if we run $H$ on $⟨D,⟨D⟩⟩$, then $H$ will accept but if we run $H$ on $⟨D,⟨D⟩^R⟩$, then $H$ will reject.

---

### 2.2

If we change the proof of `THEROM 4.11` such that on input $⟨M⟩^R$ , $D$ will run $H$ on input $⟨M,⟨M⟩⟩$, then we will still **wont** get a contradiction.

If on input $⟨M⟩^R$ $D$ run $H$ on input $⟨M,⟨M⟩⟩$, then $D(⟨D⟩)$ means: on input $⟨D⟩=⟨M'⟩^R$, where $⟨M'⟩ =⟨D⟩^R$ and $M'$ is a turing machine, $D$ run $H$ on input $⟨M',⟨M'⟩⟩ = ⟨M',⟨D⟩^R⟩$. If $⟨D⟩ = ⟨M'⟩^R$ where $M'$ is a turing machine, let $M'$ run as $D$, so that $D$ run $H$ on input $⟨D,⟨D⟩^R⟩$, and we already proved that there is no contradiction here.

**Note**: I'm assuming that due to the nature of $⟨⟩$ as a string that represent the encoding of a TM, we can represent some turing machine $M'$ that function as $D$ with $⟨D⟩^R$. If there is no TM $M' = ⟨D⟩^R$, than the proof does not hold any way.

### 2.3

If we change the proof of `THEROM 4.11` such that on input $⟨M⟩^R$ , $D$ will run $H$ on input $⟨M,⟨M⟩^R⟩$, then we **will** get a contradiction, under an assumption regarding the encoding of $D$.

If on input $⟨M⟩^R$ $D$ run $H$ on input $⟨M,⟨M⟩^R⟩$, then $D(⟨D⟩)$ means: on input $⟨D⟩=⟨M'⟩^R$, where $⟨M'⟩ =⟨D⟩^R$ and $M'$ is a turing machine, $D$ run $H$ on input $⟨M',⟨M'⟩^R⟩ = ⟨M',{⟨D⟩^R}^R⟩ = ⟨M',⟨D⟩⟩$. If we could assume that $⟨M'⟩ = ⟨D⟩$, meaning $⟨D⟩ = ⟨D⟩^R$, we would get a contradiction:

If $H$ **does not accept** $⟨M',⟨D⟩⟩$: it means $M'$ **does not accept**  $\boldsymbol{⟨D⟩}$, and thus $D$ **does** accepts  $\boldsymbol{⟨D⟩}$, wich is a contradiction under ther assumption that $⟨M'⟩ = ⟨D⟩$ and thus $M'$ and $D$ are the same TM. Same TM can't accept and reject the same input.

If $H$ accepts $⟨M',⟨D⟩⟩$:  it means $M'$ accepts  $\boldsymbol{⟨D⟩}$, and thus $D$ rejects  $\boldsymbol{⟨D⟩}$. Again no contradiction here because there might be some TM $D$ such that if we run $H$ on $⟨D,⟨D⟩⟩$, then $H$ will accept but if we run $H$ on $⟨D,⟨D⟩^R⟩$, then $H$ will reject.

## Question 3

We will use the the `Diagonalization` method to build a TM $K$ such that $L(K) = \{w | K \ stops \ on \ input \ w \ with \ f(w) \ on \ the \ tape \}$, where $f_k(w)$ is the function that $K$ computes, and $f_k(w)\neq f_i(w)$ for all $i$ functions that TM $M_i$ computes where $⟨M_i⟩ \in A$.

We will use an `enumaration` of all the TM's $M_i$ that are in $A$, and we will build a TM $K$ that will compute a function $f_k(w)$ that is different from all the functions that $M_i$ computes.

The enumeration of all the TM's $M_i$ that are in $A$ is possible because $A$ is enumerable, and thus we can build a TM $E$ that will enumerate all the TM's $M_i$ that are in $A$. We can then build $K$ that will use $E$ to enumerate all the TM's $M_i$ that are in $A$ and compute a function $f_k(w)$ that is different from all the functions that $M_i$ computes.

We will build $K$ such that on input $w$:
1. Use $E$ to enumerate all the TM's $M_i$ that are in $A$.
2. On every $i$ TM $M_i$ that $⟨M_i⟩ \in A$:
    1. Run $M_i$ on $w$.
    2. If $M_i$ accepts $w$, then reject.
    3. If $M_i$ rejects $w$, then accept.
      ($M$ does not halt on $w$ because $M_i$ does not halt on $w$.)

The function $f_k(w)$ that $K$ computes is different from all the functions that $M_i$ computes because $K$ will always reject on input $w$ if $M_i$ accepts $w$, and will always accept on input $w$ if $M_i$ rejects $w$. So $K$ will always compute a different function from all the functions that $M_i$ computes. In addition, there is no TM $M_i$ in $A$ that computes $f_k(w)$ because the way $K$ computes $f_k(w)$ is by rejecting on input $w$ if $M_i$ accepts $w$, and accepting on input $w$ if $M_i$ rejects $w$, and thus $K$ will never accept on input $w$ if $M_i$ accepts $w$, and will never reject on input $w$ if $M_i$ rejects $w$. If there is a TM $M_i$ in $A$ that computes $f_k(w)$, then $K$ will simply keep runing $M_i$ on $w$ and will never halt, and thus $K$ will not compute $f_k(w)$.

## Question 4

Let $AGREE_{TM} = \{⟨M_1,M_2⟩ | M_1 \ and \ M_2 \ are \ TM's \ and \ there \ is \ at \ least \ one \ input \ word \ w \ such \ that \ M_1 \ and \ M_2 \ both \ accept \ w \ or \ both \ dont \ accept \ w\}$

We will show that $AGREE_{TM}$ is undecidable by showing that $A_{TM}$ is reducible to $AGREE_{TM}$.

We will use the following reduction $F$ from $A_{TM}$ to $AGREE_{TM}$:

$F = \ on \ input \ ⟨M,w⟩:$
1. $Build \ a \ TM \ M_1 \ such \ that:$
    1. $M_1 \ on \ input \ x:$
        1. Run $M$ on $w$.
        2. If $M$ accepts $w$, then accept.
    2. $Build \ a \ TM \ M_2 \ such \ that:$
        1. $M_2 \ on \ input \ x:$
        1. Accept.
   1. $Return \ ⟨M_1,M_2⟩$

If $M \notin A_tm$, meanin M does not accept $w$, then $M_1$ will  not halt on $w$, and since $M_2$ always accept, $M_1$ and $M_2$ do not agree on $w$. For any input ⟨M,w⟩ that $M$ does not accept, we can thus build $M_1$ and $M_2$ such that $M_1$ and $M_2$ do not agree on the acceptance of $w$. Note that we can also  implement this on any other input word $x \neq w$ so that $M_1$ and $M_2$ will not agree on the acceptance of $x$.

On the other hand, if $M$ **does** halt on $w$, then $M_1$ will also halt and accept on $w$, and since $M_2$ always accept, $M_1$ and $M_2$ agree on the acceptance of $w$ only if $M$ accepts $w$. Therefore, $⟨M_1, M_2⟩ \in AGREE_{TM}$ if and only if $⟨M, w⟩ \in A_{TM}$.

So $F$ is a reduction from $A_{TM}$ to $AGREE_{TM}$, and since $A_{TM}$ is undecidable, $AGREE_{TM}$ is undecidable.

Note: this question remind me logical gates and the way we can build any logical gate from NAND gate. We can build any TM from NAND gate, and we can build any TM from $AGREE_{TM}$.

## Question 5

### 5.1

$A_{TM} = \{⟨M,w⟩ | M \ is \ a \ TM \ and \ M \ \textbf{accepts} \ w\}$

$LOOP-ONE = \{⟨M⟩ | M \ is \ a \ TM \ and \ M \ does \ not \ halt \ on \ exactly \ one \ input \ word\}$

The following $F_1$ is a reduction from $A_{TM}$ to $LOOP-ONE$:

$F_1 = \ on \ input \ ⟨M,w⟩:$
1. $Build \ a \ TM \ M' \ such \ that:$
    1. Cut $M$ transition function relevant to $w$ to a function that on $w$, instead of moving to accept state moves on $w$ to loop state. Add rejects to every other input word (incluiding w if didn't accept - add the loop only by replacing the accept).
    2. $Return \ ⟨M'⟩$

Validity of $F_1$:

If $⟨M,w⟩ \in A_{TM}$, then $M$ accepts $w$, and thus $M'$ does not halt on exactly one input word: $w$. On every other input word $M'$ will accept, and thus $⟨M'⟩ \in LOOP-ONE$.

If $⟨M,w⟩ \notin A_{TM}$, then $M$ will never loop, and thus $⟨M'⟩ \notin LOOP-ONE$.

### 5.2

$\bar A_{TM} = \{⟨M,w⟩ | M \ is \ a \ TM \ and \ M \ \textbf{does \ not \ accept} \ w\}$

The following $F_2$ is a reduction from $\bar A_{TM}$ to $LOOP-ONE$:

$F_2 = \ on \ input \ ⟨M,w⟩:$
1. $Build \ a \ TM \ M' \ such \ that:$
    1. $M' \ on \ input \ x:$
        1. If $x \neq w$, then accept.
        2. Run $M$ on $w$.
        3. If $M$ accepts $w$, then accept.
    2. $Return \ ⟨M'⟩$

Validity of $F_2$:

If $⟨M,w⟩ \in \bar A_{TM}$, then $M$ can loop or reject on $w$, and thus $M'$ does not halt on exactly one input word: $w$. On every other input word $M'$ will accept, and thus $⟨M'⟩ \in LOOP-ONE$ if $⟨M,w⟩ \in \bar A_{TM}$.

If $⟨M,w⟩ \notin \bar A_{TM}$, then $M$ will accept $w$, and thus $M'$ will never halt on $w$, and thus $⟨M'⟩ \notin LOOP-ONE$.

### 5.3

Again for convinience, $LOOP-ONE = \{⟨M⟩ | M \ is \ a \ TM \ and \ M \ does \ not \ halt \ on \ exactly \ one \ input \ word\}$)

$ALL_{TM} = \{⟨M⟩ | M \ is \ a \ TM \ and \ L(M) = \Sigma^*\}$

The following F_3 is a reduction from $ALL_{TM}$ to $LOOP-ONE$:

$F_3 = \ on \ input \ ⟨M⟩:$
1. $Build \ a \ TM \ M' \ such \ that:$
    1. $M' \ on \ input \ x:$
        1. Run $M$ on every word $w$ in $\Sigma^*$ except $⟨M⟩$ in lexicographic order.
        2. if $M$ doesnt accept a word $w$, then accept.
        3. Run $M$ on $⟨M⟩$.
        4. If $M$ accepts $⟨M⟩$ (and also all words), then loop.
        5. Else, accept.
    2. $Return \ ⟨M'⟩$

Validity of $F_3$:

What $M'$ does is to return a modified version of $M$ that does not halt on exactly one input word: its own encoding $⟨M⟩$. If $⟨M⟩ \in ALL_{TM}$, then $M$ accepts every word in $\Sigma^*$, in particular it accepts $⟨M⟩$. Since $M$ accepts all words, it halts on every word so $M'$ will use this attribute and mach a specific word that $M'$ will loop upon. It can be done by modifying $M$ transition function to a function that instead of accepting on input $⟨M⟩$: will loop.

If $⟨M⟩ \notin ALL_{TM}$, then $M'$ will always halt and thus $\notin LOOP-ONE$. If $M$ reject or loop on any word $w \neq ⟨M⟩$
 in $\Sigma^*$, then $M'$ will halt on that word and accept (can also reject intead). If $M$ does not accept $⟨M⟩$, then $M'$ will also halt on $⟨M⟩$ and accept and also If $M$ loops on $⟨M⟩$.

The only case that $M'$ will not halt is if $M$ accepts all words in $\Sigma^*$ and also $⟨M⟩$, and thus $M'$ will loop only on $⟨M⟩$ and not halt on exactly one input word.
