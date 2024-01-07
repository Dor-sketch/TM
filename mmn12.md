# mmn12

## Question 1

### 1.1

$M$ dosn not decide any language, because it does not reject any input. According to the definition of a langugae that is decided by a TM, TM must be a decider - a TM that `always make a decision to accept or reject. A decider that regonize some langugae also is said to decide that langugae.` (Sipser, 2006, p. 170) So in the case of non-decider TM, it does not decide any language, thus the language $L$ that $M$ decides is _not existing_, or $L(M) = \emptyset$.

**Question:** Can we talk about a language that is decided by a TM that is not a decider? Formally, I thoght the `decide` is a property of only decider TM.

### 1.2

$M$ accepts the languguage of string such that each string represent encoding of a context free grammar that generates at least one word. Formally, $L(M) = \{<G> | G \ is \ a \ CFG \ and \ L(G) \neq \emptyset \}$. This is because $M$ accepts the encoding of G, only if there is word $w$ such that $<G,w>\in  A_{CFG}$, and according to the definition of $A_{CFG}$ from p. 198,  $<G,w>\in  A_{CFG}$ if and only if $w\in L(G)$, so $M$ accepts $<G>$ if and only if $L(G) \neq \emptyset$.

## Question 2

### 2.1

If we change the proof of `THEROM 4.11` such that $D$ will run $H$ on input $<M,<M>^R>$, then we **wont** get a contradiction. On input $<D>$ $D$ will run $H$ on input $<D,<D>^R>$.

We will break the options for $D(<D>)$:

---

If $H$ **does not accept** $<D,<D>^R>$:

it means $D$ **does not accept**  $\boldsymbol{<D>^R}$, and thus $D$ **does** accepts  $\boldsymbol{<D>}$, wich is not a contradiction because there might be some TM $D$ such that if we run $H$ on $<D,<D>>$, then $H$ will accept but if we run $H$ on $<D,<D>^R>$, then $H$ will reject.

---

If $H$ accepts $<D,<D>^R>$:

it means $D$ accepts  $\boldsymbol{<D>^R}$, and thus $D$ rejects  $\boldsymbol{<D>}$. Again no contradiction here because there might be some TM $D$ such that if we run $H$ on $<D,<D>>$, then $H$ will accept but if we run $H$ on $<D,<D>^R>$, then $H$ will reject.

---

### 2.2

If we change the proof of `THEROM 4.11` such that on input $<M>^R$ , $D$ will run $H$ on input $<M,<M>>$, then we will still **wont** get a contradiction.

If on input $<M>^R$ $D$ run $H$ on input $<M,<M>>$, then $D(<D>)$ means: on input $<D>=<M'>^R$, where $<M'> =<D>^R$ and $M'$ is a turing machine, $D$ run $H$ on input $<M',<M'>> = <M',<D>^R>$. If $<D> = <M'>^R$ where $M'$ is a turing machine, let $M'$ run as $D$, so that $D$ run $H$ on input $<D,<D>^R>$, and we already proved that there is no contradiction here.

**Note**: I'm assuming that due to the nature of $<>$ as a string that represent the encoding of a TM, we can represent some turing machine $M'$ that function as $D$ with $<D>^R$. If there is no TM $M' = <D>^R$, than the proof does not hold any way.

## 2.3

If we change the proof of `THEROM 4.11` such that on input $<M>^R$ , $D$ will run $H$ on input $<M,<M>^R>$, then we **will** get a contradiction, under an assumption regarding the encoding of $D$.

If on input $<M>^R$ $D$ run $H$ on input $<M,<M>^R>$, then $D(<D>)$ means: on input $<D>=<M'>^R$, where $<M'> =<D>^R$ and $M'$ is a turing machine, $D$ run $H$ on input $<M',<M'>^R> = <M',{<D>^R}^R> = <M',<D>>$. If we could assume that $<M'> = <D>$, meaning $<D> = <D>^R$, we would get a contradiction:

If $H$ **does not accept** $<M',<D>>$: it means $M'$ **does not accept**  $\boldsymbol{<D>}$, and thus $D$ **does** accepts  $\boldsymbol{<D>}$, wich is a contradiction under ther assumption that $<M'> = <D>$ and thus $M'$ and $D$ are the same TM. Same TM can't accept and reject the same input.

If $H$ accepts $<M',<D>>$:  it means $M'$ accepts  $\boldsymbol{<D>}$, and thus $D$ rejects  $\boldsymbol{<D>}$. Again no contradiction here because there might be some TM $D$ such that if we run $H$ on $<D,<D>>$, then $H$ will accept but if we run $H$ on $<D,<D>^R>$, then $H$ will reject.

## Question 3

We will use the the `Diagonalization` method to build a TM $K$ such that $L(K) = \{w | K \ stops \ on \ input \ w \ with \ f(w) \ on \ the \ tape \}$, where $f_k(w)$ is the function that $K$ computes, and $f_k(w)\neq f_i(w)$ for all $i$ functions that TM $M_i$ computes where $<M_i> \in A$.

We will use an enumaration of all the TM's $M_i$ that are in $A$, and we will build a TM $K$ that will compute a function $f_k(w)$ that is different from all the functions that $M_i$ computes.


## Question 4

## Question 5

