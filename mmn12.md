# mmn12

## Question 1

### 1.1

$M$ dosn not decide any language, because it does not reject any input. According to the definition of a langugae that is decided by a TM, TM must be a decider - a TM that `always make a decision to accept or reject. A decider that regonize some langugae also is said to decide that langugae.` (Sipser, 2006, p. 170) So in the case of non-decider TM, it does not decide any language, thus the language $L$ that $M$ decides is _not existing_, or $L(M) = \emptyset$.

**Question:** Can we talk about a language that is decided by a TM that is not a decider? Formally, I thoght the `decide` is a property of only decider TM.

### 1.2

$M$ accepts the languguage of string such that each string represent encoding of a context free grammar that generates at least one word. Formally, $L(M) = \{<G> | G \ is \ a \ CFG \ and \ L(G) \neq \emptyset \}$. This is because $M$ accepts the encoding of G, only if there is word $w$ such that $<G,w>\in  A_{CFG}$, and according to the definition of $A_{CFG}$ from p. 198,  $<G,w>\in  A_{CFG}$ if and only if $w\in L(G)$, so $M$ accepts $<G>$ if and only if $L(G) \neq \emptyset$.

## Question 2

