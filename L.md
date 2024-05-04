# Important Languages


<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Important Languages](#important-languages)
  - [Chapter 4: Decidability](#chapter-4-decidability)
    - [$A_{DFA} = \{⟨A, w⟩ | A \text{ is a DFA and } A \text{ accepts } w\}$](#a_dfa--a-w--a-text-is-a-dfa-and--a-text-accepts--w)
    - [$A_{NFA} = \{⟨A, w⟩ | A \text{ is a NFA and } A \text{ accepts } w\}$](#a_nfa--a-w--a-text-is-a-nfa-and--a-text-accepts--w)
    - [$A_{REX} = \{⟨R, w⟩ | R \text{ is a regular expression and } R \text{ generates } w\}$](#a_rex--r-w--r-text-is-a-regular-expression-and--r-text-generates--w)
    - [$E_{DFA} = \{⟨A⟩ | A \text{ is a DFA and } L(A) = \emptyset\}$](#e_dfa--a--a-text-is-a-dfa-and--la--emptyset)
    - [$EQ_{DFA} = \{⟨A, B⟩ | A \text{ and } B \text{ are DFAs and } L(A) = L(B)\}$](#eq_dfa--a-b--a-text-and--b-text-are-dfas-and--la--lb)
    - [$EQ_{LBA} = \{⟨M_1, M_2⟩ | M_1 \text{ and } M_2 \text{ are LBAs and } L(M_1) = L(M_2)\}$](#eq_lba--m_1-m_2--m_1-text-and--m_2-text-are-lbas-and--lm_1--lm_2)
    - [$A_{CFG} = \{⟨G, w⟩ | G \text{ is a CFG and } G \text{ generates } w\}$](#a_cfg--g-w--g-text-is-a-cfg-and--g-text-generates--w)
    - [$\bar{A}_{CFG} = \{⟨G, w⟩ | G \text{ is a CFG and } G \text{ does not generate } w\}$](#bara_cfg--g-w--g-text-is-a-cfg-and--g-text-does-not-generate--w)
    - [$E_{CFG} = \{⟨G⟩ | G \text{ is a CFG and } L(G) = \emptyset\}$](#e_cfg--g--g-text-is-a-cfg-and--lg--emptyset)
    - [$EQ_{CFG} = \{⟨G_1, G_2⟩ | G_1 \text{ and } G_2 \text{ are CFGs and } L(G_1) = L(G_2)\}$](#eq_cfg--g_1-g_2--g_1-text-and--g_2-text-are-cfgs-and--lg_1--lg_2)
    - [$A_{TM} = \{⟨M, w⟩ | M \text{ is a TM and } M \text{ accepts } w\}$](#a_tm--m-w--m-text-is-a-tm-and--m-text-accepts--w)
    - [$\bar{A}_{TM} = \{⟨M, w⟩ | M \text{ is a TM and } M \text{ does not accept } w\}$](#bara_tm--m-w--m-text-is-a-tm-and--m-text-does-not-accept--w)
  - [Chapter 5: Reducibility](#chapter-5-reducibility)
    - [$HALT_{TM} = \{⟨M, w⟩ | M \text{ is a TM and } M \text{ halts on input } w\}$](#halt_tm--m-w--m-text-is-a-tm-and--m-text-halts-on-input--w)
      - [a. Turing Reduction](#a-turing-reduction)
    - [$\bar{E}_{TM} = \{⟨M⟩ | M \text{ is a TM and } L(M) \neq \emptyset\}$](#bare_tm--m--m-text-is-a-tm-and--lm-neq-emptyset)
      - [Problem 4.5: Proof that $\bar{E}_{TM}$ is recognizable by building a TM that recognizes it](#problem-45-proof-that-bare_tm-is-recognizable-by-building-a-tm-that-recognizes-it)
    - [$E_{TM} = \{⟨M⟩ | M \text{ is a TM and } L(M) = \emptyset\}$](#e_tm--m--m-text-is-a-tm-and--lm--emptyset)
      - [Proof that $E_{TM}$ is undecidable using $S$ style reduction to $A_{TM}$](#proof-that-e_tm-is-undecidable-using-s-style-reduction-to-a_tm)
      - [Proof that $E_TM$ is Unrecognizable using $THEROM \ 4.22$](#proof-that-e_tm-is-unrecognizable-using-therom--422)
      - [Proof that $E_tm$ is Unrecognizable using complement mapping](#proof-that-e_tm-is-unrecognizable-using-complement-mapping)
    - [$REGULAR_{TM} = \{⟨M⟩ | M \text{ is a TM and } L(M) \text{ is a regular language}\}$](#regular_tm--m--m-text-is-a-tm-and--lm-text-is-a-regular-language)
    - [$EQ_{TM} = \{⟨M_1, M_2⟩ | M_1 \text{ and } M_2 \text{ are TMs and } L(M_1) = L(M_2)\}$](#eq_tm--m_1-m_2--m_1-text-and--m_2-text-are-tms-and--lm_1--lm_2)
    - [$A_{LBA} = \{⟨M, w⟩ | M \text{ is a LBA and } M \text{ accepts } w\}$](#a_lba--m-w--m-text-is-a-lba-and--m-text-accepts--w)
    - [$\bar{A}_{LBA} = \{⟨M, w⟩ | M \text{ is a LBA and } M \text{ does not accept } w\}$](#bara_lba--m-w--m-text-is-a-lba-and--m-text-does-not-accept--w)
    - [$E_{LBA} = \{⟨M⟩ | M \text{ is a LBA and } L(M) = \emptyset\}$](#e_lba--m--m-text-is-a-lba-and--lm--emptyset)
    - [$\bar{E}_{LBA} = \{⟨M⟩ | M \text{ is a LBA and } L(M) \neq \emptyset\}$](#bare_lba--m--m-text-is-a-lba-and--lm-neq-emptyset)
    - [$ALL_{CFG} = \{⟨G⟩ | G \text{ is a CFG and } L(G) = \Sigma^*\}$](#all_cfg--g--g-text-is-a-cfg-and--lg--sigma)
  - [Chapter 7: Time Complexity](#chapter-7-time-complexity)
    - [$HAMPATH = \{⟨G, u, v⟩ | G \text{ is a directed graph that contains a Hamiltonian path from } u \text{ to } v\}$](#hampath--g-u-v--g-text-is-a-directed-graph-that-contains-a-hamiltonian-path-from--u-text-to--v)
    - [$COMPOSITE = \{⟨n⟩ | n \text{ is a composite number}\}$](#composite--n--n-text-is-a-composite-number)
    - [$CLIQUE = \{⟨G, k⟩ | G \text{ is an undirected graph with a clique of size } k\}$](#clique--g-k--g-text-is-an-undirected-graph-with-a-clique-of-size--k)
    - [$SUBSET-SUM = \{⟨S, t⟩ | S \text{ is a set of integers and there is a subset of S that sums to } t\}$](#subset-sum--s-t--s-text-is-a-set-of-integers-and-there-is-a-subset-of-s-that-sums-to--t)
    - [$SAT = \{⟨\phi⟩ | \phi \text{ is a Boolean formula that is satisfiable}\}$](#sat--phi--phi-text-is-a-boolean-formula-that-is-satisfiable)
    - [$ALL_{DFA} = \{⟨A⟩ | A \text{ is a DFA and } L(A) = \Sigma^*\}$](#all_dfa--a--a-text-is-a-dfa-and--la--sigma)
  - [Chapter 8: Space Complexity](#chapter-8-space-complexity)
    - [$ALL_{NFA} = \{⟨A⟩ | A \text{ is a NFA and } L(A) = \Sigma^* \}$](#all_nfa--a--a-text-is-a-nfa-and--la--sigma-)
    - [$EQ_{REX} = \{⟨R_1, R_2⟩ | R_1 \text{ and } R_2 \text{ are regular expressions and } L(R_1) = L(R_2)\}$](#eq_rex--r_1-r_2--r_1-text-and--r_2-text-are-regular-expressions-and--lr_1--lr_2)

<!-- /code_chunk_output -->



## Chapter 4: Decidability

### $A_{DFA} = \{⟨A, w⟩ | A \text{ is a DFA and } A \text{ accepts } w\}$

where: p. 194

Description: The language of all DFAs that accept a string $w$

Type: Decidable

Proof (p. 194): The TM $M$ that decides $A_{DFA}$:

$M = "On input ⟨B, w⟩, where B \text{ is a DFA and } w \text{ is a string}:$

1. Run B on input w. (Simulate B on w)
2. If B accepts, accept; otherwise, reject."

---

### $A_{NFA} = \{⟨A, w⟩ | A \text{ is a NFA and } A \text{ accepts } w\}$

where: p. 195

Description: The language of all NFAs (Nondeterministic Finite Automata) that accept a string $w$

Type: Decidable

Proof (p. 195): The TM $N$ that decides $A_{NFA}$:

$N = "On input ⟨B, w⟩, where B \text{ is a NFA and } w \text{ is a string}:$

1. Convert NFA B to an equivalent DFA C using the subset construction.
2. Run TM $M$ on input ⟨C, w⟩, where $M$ is the TM that decides $A_{DFA}$.
3. If M accepts, accept; otherwise, reject."

---

### $A_{REX} = \{⟨R, w⟩ | R \text{ is a regular expression and } R \text{ generates } w\}$

Description: The language of all regular expressions that generate a string $w$

where: p. 196

Type: Decidable

Proof (p. 196): The idea is to convert the regular expression $R$ to a NFA $A$ and then simulate $A$ on $w$. If $A$ accepts $w$, then $R$ generates $w$.

PROOF: The TM $P$ that decides $A_{REX}$:

$P = "On input ⟨R, w⟩, where R \text{ is a regular expression and } w \text{ is a string}:$

1. Convert R to an equivalent NFA A.
2. Run NFA A on input w.
3. If A accepts, accept; otherwise, reject."

---

### $E_{DFA} = \{⟨A⟩ | A \text{ is a DFA and } L(A) = \emptyset\}$

where: p. 196

Description: The language of all DFAs that accept the empty language

Type: Decidable

Proof (p. 196): The TM $Q$ that decides $E_{DFA}$:

$Q = "On input ⟨B⟩, where B \text{ is a DFA}:$

1. Construct the DFA C that is the complement of B.
2. Run TM $M$ on input ⟨C, w⟩, where $M$ is the TM that decides $A_{DFA}$.
3. If M accepts, accept; otherwise, reject."

---

### $EQ_{DFA} = \{⟨A, B⟩ | A \text{ and } B \text{ are DFAs and } L(A) = L(B)\}$

where: p. ?

Description: The language of all pairs of DFAs that generate the same language

Type: Decidable

Proof (p. 196): The TM $D$ that decides $EQ_{DFA}$:

$D = "On input ⟨A, B⟩, where A \text{ and } B \text{ are DFAs}:$

1. Construct the DFA C that is the symmetric difference of A and B.
2. Run TM $M$ on input ⟨C, w⟩, where $M$ is the TM that decides $A_{DFA}$.
3. If M accepts, accept; otherwise, reject."

---

### $EQ_{LBA} = \{⟨M_1, M_2⟩ | M_1 \text{ and } M_2 \text{ are LBAs and } L(M_1) = L(M_2)\}$

where: ?

Description: The language of all pairs of Linear Bounded Automata that generate the same language

Type: Unrecognizable

---

### $A_{CFG} = \{⟨G, w⟩ | G \text{ is a CFG and } G \text{ generates } w\}$

where: p. 198

Description: The language of all Context-Free Grammars that generate a string $w$

Type: Decidable

Proof (p. 198): The hard part is the number of derivations. We can convert the CFG $G$ to Chomsky Normal Form, where each word had at most $2n-1$ derivations. We can then generate all derivations of length $2n-1$ and check if any of them generate $w$.

PROOF: The TM S for $A_{CFG}$

S = "On input $⟨G, w⟩$, where $G$ is a CFG and $w$ is a string:

1. Convert $G$ to Chomsky Normal Form.
2. Enumerate all derivations of length $2n-1$, aka , list all derivations with $2n-1$ steps (if $|w| = 0$, then $n = 1$).
3. If any derivation generates $w$, accept; otherwise, reject."

---

Time ?

Space ?

### $\bar{A}_{CFG} = \{⟨G, w⟩ | G \text{ is a CFG and } G \text{ does not generate } w\}$

Description: The language of all Context-Free Grammars that do not generate a string $w$

Type: Decidable

Proof: The complement of $A_{CFG}$ is decidable because we can use the same TM $S$ for $A_{CFG}$ and just change the accept/reject conditions.

---

### $E_{CFG} = \{⟨G⟩ | G \text{ is a CFG and } L(G) = \emptyset\}$

where: p. 199

Description: The language of all Context-Free Grammars that generate the empty language

Type: Decidable

Proof (p. 199): The TM $T$ that decides $E_{CFG}$:

$T = "On input ⟨G⟩, where G \text{ is a CFG}:$

1. Construct the CNF of G.
2. Enumerate all derivations of length $2n-1$.
3. If any derivation generates a string, reject; otherwise, accept."
4. If $|w| = 0$, then $n = 1$.
5. If any derivation generates $w$, accept; otherwise, reject."
6. If any derivation generates $w$, accept; otherwise, reject."

---

### $EQ_{CFG} = \{⟨G_1, G_2⟩ | G_1 \text{ and } G_2 \text{ are CFGs and } L(G_1) = L(G_2)\}$

where: p. 200

Description: The language of all pairs of Context-Free Grammars that generate the same language

Type: Undecidable

---

### $A_{TM} = \{⟨M, w⟩ | M \text{ is a TM and } M \text{ accepts } w\}$

where: p. 202

Description: The language of all Turing Machines that accept a string $w$

Type: Undecidable

Proof: Use the diagonalization method to prove that $A_{TM}$ is undecidable. Suppose there is a TM $H$ that decides $A_{TM}$. We can Construct a word $w$ that is not in $A_{TM}$ as follows:

1. Enumerate all strings $w_1, w_2, w_3, ...$ in $\Sigma^*$.
2. For each $i$, run $H$ on $⟨M_i, w_i⟩$, where $M_i$ is the $i$th TM in the enumeration.
3. If $H$ accepts $⟨M_i, w_i⟩$, then $w_i$ is not in $A_{TM}$.
4. If $H$ rejects $⟨M_i, w_i⟩$, then $w_i$ is in $A_{TM}$.
5. Construct a word $w$ that is not in $A_{TM}$ by taking the $i$th character of $w_i$ and changing it to a different character.
6. $H$ cannot decide whether $w$ is in $A_{TM}$, because $w$ is constructed to be different from all $w_i$.
7. Therefore, $A_{TM}$ is undecidable.

---

Time complexity: N/A

Space complexity: N/A

### $\bar{A}_{TM} = \{⟨M, w⟩ | M \text{ is a TM and } M \text{ does not accept } w\}$

Description: The language of all Turing Machines that do not accept a string $w$

Type: Recognizable

---

## Chapter 5: Reducibility

### $HALT_{TM} = \{⟨M, w⟩ | M \text{ is a TM and } M \text{ halts on input } w\}$

p. 216

Description: The language of all Turing Machines that halt on input $w$

$HALT_{TM} = \{⟨M, w⟩ | M \text{ is a TM and } M \text{ halts on input } w\}$

Description: The language of all Turing Machines that halt on input $w$

Type: Undecidable

Proof:

#### a. Turing Reduction

Let's assume that there is some TM $R$ that decides $HALT_{TM}$. We construct a TM $S$ that decides $A_{TM}$ as follows:

$S = "On input ⟨M, w⟩, where M \text{ is a TM and } w \text{ is a string}:$

1. Run TM $R$ on input ⟨M, w⟩.
2. If $R$ rejects, reject.
3. If $R$ accepts, simulate $M$ on input $w$ until it halts.
4. If $M$ accepts, accept; otherwise, reject."

If $R$ decides $HALT_{TM}$, then $S$ decides $A_{TM}$, but $A_{TM}$ is undecidable, so $R$ cannot exist and $HALT_{TM}$ is undecidable.

---

Time complexity: N/A

Space complexity: N/A

---

### $\bar{E}_{TM} = \{⟨M⟩ | M \text{ is a TM and } L(M) \neq \emptyset\}$

Description: The language of all Turing Machines that do not accept the empty language

p. 211 q 4.5

Type: Recognized

#### Problem 4.5: Proof that $\bar{E}_{TM}$ is recognizable by building a TM that recognizes it

Let $s_1, s_2, s_3, ...$ be an enumeration of all strings in $\Sigma^*$. We can build a TM $R$ that recognizes $\bar{E}_{TM}$ as follows:

$$
\begin{align*}
R = & \text{"On input } ⟨M⟩, \text{ where } M \text{ is a TM:} \\
& \text{1. For } i = 1, 2, 3, ... \\
& \text{2. Run } M \text{ on } s_i. \\
& \text{3. If } M \text{ accepts } s_i, \text{ accept.}
\end{align*}
$$

If $M$ accepts any string $s_i$, then $R$ will accept $M$. Therefore, $R$ recognizes $\bar{E}_{TM}$.

Kind of like BFS - we check all strings of length 1, then all strings of length 2, and so on.

### $E_{TM} = \{⟨M⟩ | M \text{ is a TM and } L(M) = \emptyset\}$

where: p. 217

Description: The language of all Turing Machines that accept the empty language

Type: Unrecognizable

#### Proof that $E_{TM}$ is undecidable using $S$ style reduction to $A_{TM}$

Proof: Suppose there is a TM $R$ that decides $E_{TM}$. We can use $R$ to decide $A_{TM}$ as follows:
The main idea is to check if $R$ accepts - if it does, then the input TM doesn't accept any strings, and if it doesn't, then the input TM accepts at least one string.
We modify the input TM to accept only one string, and then we check on the modifyied $M = M'$ if $R$ accepts. If it does, then the original TM doesn't accept any strings, and if it doesn't... (see below)

Let the following TM be the modifyied TM $M_1$:
$$
\begin{align*}
M_1 = & \text{"On input x:"} \\
& \text{1. if } x\neq w, \text{ reject.} \\
& \text{2. If } x = w, \text{ run M on input w and accept if M accepts.}
\end{align*}
$$

Now we construct $S$ that decides $A_{TM}$ as follows:
$$
\begin{align*}
S = & \text{"On input ⟨M, w⟩, where M is a TM and w is a string:"} \\
& \text{1. Construct the TM } M_1 \text{ as described above.} \\
& \text{2. Run R on input } ⟨M_{1}⟩ \text{.} \\
& \text{3. If R accepts, reject; otherwise, accept.}
\end{align*}
$$

$S$ decides $A_{TM}$, but $A_{TM}$ is undecidable, so $R$ cannot exist.

#### Proof that $E_TM$ is Unrecognizable using $THEROM \ 4.22$

From problem 4.5  $\bar{E}_{TM}$ is recognizable. So if $E_TM$ is recognizable, than according to 4.22 $E_TM$ id decidable, and thats a construction.

#### Proof that $E_tm$ is Unrecognizable using complement mapping

Let's assume that $E_TM$ is r

---

Time complexity: N/A

Space complexity: N/A

---

### $REGULAR_{TM} = \{⟨M⟩ | M \text{ is a TM and } L(M) \text{ is a regular language}\}$

p. 218

Description: The language of all Turing Machines that accept a regular language

Type: Undecidable

Proof: Suppose there is a TM $H$ that decides $REGULAR_{TM}$. We can use $H$ to decide $E_{TM}$ as follows:

On input $⟨M⟩$, where $M$ is a TM:

1. Construct the following TM $M'$:
2. $M'$ = "On input $x$:
3. Run $M$ on $x$.
4. If $M$ accepts, accept."
5. If $H$ accepts $⟨M'⟩$ then accept, otherwise reject.
6. $H$ decides $REGULAR_{TM}$, but $REGULAR_{TM}$ is undecidable, so $H$ cannot exist.
7. Therefore, $REGULAR_{TM}$ is undecidable.

---

Time complexity: N/A

Space complexity: N/A

---

### $EQ_{TM} = \{⟨M_1, M_2⟩ | M_1 \text{ and } M_2 \text{ are TMs and } L(M_1) = L(M_2)\}$

where: p. 220

Description: The language of all pairs of Turing Machines that generate the same language

Type: Undecidable

Proof: Suppose there is a TM $H$ that decides $EQ_{TM}$. We can use $H$ to decide $E_{TM}$ as follows:

---

### $A_{LBA} = \{⟨M, w⟩ | M \text{ is a LBA and } M \text{ accepts } w\}$

p.222

Description: The language of all Linear Bounded Automata that accept a string $w$

Type: Decidable

Proof (p. 222): The idea is to track weather the LBA is in a loop or not. If it is, then it will never accept the string. If it is not, then it will accept or reject the string in a finite number of steps. The total number of configurations is finite, so we can check if the LBA is in a loop. The number is $qng^n$, where $q$ is the number of states, $n$ is the length of the the tape, and $g^n$ is the number of possible tape contents (possible strings of tape symbols apear on the tape). With a tape of length $n$, $qng^n$ is thus the total number of different configurations of $M$ with a tape of length $n$.

Algorithm $L$ that decides $A_{LBA}$:
L = "On input $⟨M, w⟩$, where $M$ is a LBA and $w$ is a string:
1. Simulate $M$ on input $w$ for $qng^n$ steps or until it halts, where $q$ is the number of states, $n$ is the length of the tape, and $g$ is the number of tape symbols.
2. If M has halted, accept if it is in an accept state; otherwise, reject.

If we passed the $qng^n$ steps, then we know that the LBA is in a loop and will never accept the string.

---

Space complexity: PSPACE-COMPLETENESS

### $\bar{A}_{LBA} = \{⟨M, w⟩ | M \text{ is a LBA and } M \text{ does not accept } w\}$

Description: The language of all Linear Bounded Automata that do not accept a string $w$

Type: Decidable

---

### $E_{LBA} = \{⟨M⟩ | M \text{ is a LBA and } L(M) = \emptyset\}$

where: p 223

Description: The language of all Linear Bounded Automata that accept the empty language

Type: Unrecognized

---

### $\bar{E}_{LBA} = \{⟨M⟩ | M \text{ is a LBA and } L(M) \neq \emptyset\}$

Description: The language of all Linear Bounded Automata that do not accept the empty language

Type: Recognizable

---

### $ALL_{CFG} = \{⟨G⟩ | G \text{ is a CFG and } L(G) = \Sigma^*\}$

where p. 225

Description: The language of all Context-Free Grammars that generate all strings

Type: Undecidable

Proof: Use the diagonalization method to prove that $ALL_{CFG}$ is undecidable. Suppose there is a TM $H$ that decides $ALL_{CFG}$. We can Construct a CFG $G$ that generates all strings as follows:

---

## Chapter 7: Time Complexity

### $HAMPATH = \{⟨G, u, v⟩ | G \text{ is a directed graph that contains a Hamiltonian path from } u \text{ to } v\}$

where: p. 292

---

### $COMPOSITE = \{⟨n⟩ | n \text{ is a composite number}\}$

where: p. 293

Description: The language of all composite numbers

Type: Decidable

---

### $CLIQUE = \{⟨G, k⟩ | G \text{ is an undirected graph with a clique of size } k\}$

Where: p. 296

Description: The language of all undirected graphs that contain a clique of size $k$

type: Decidable
Time complexity: O($n^k$) - where $n$ is the number of vertices in the graph
Family: NP-Complete

Space: ?

### $SUBSET-SUM = \{⟨S, t⟩ | S \text{ is a set of integers and there is a subset of S that sums to } t\}$

where: p. 297

---

### $SAT = \{⟨\phi⟩ | \phi \text{ is a Boolean formula that is satisfiable}\}$

where: p. 299

Description: The language of all satisfiable Boolean formulas

Type: NP-Complete

---

### $ALL_{DFA} = \{⟨A⟩ | A \text{ is a DFA and } L(A) = \Sigma^*\}$

where: p. 323

Description: The language of all DFAs that accept all strings

Type: Decidable
Time complexity: O($n$) - where $n$ is the number of states in the DFA
Family: P
SPACE_Family: PSPACE

## Chapter 8: Space Complexity

### $ALL_{NFA} = \{⟨A⟩ | A \text{ is a NFA and } L(A) = \Sigma^* \}$

where: p. 333

Description: The language of all NFAs that accept all strings

### $EQ_{REX} = \{⟨R_1, R_2⟩ | R_1 \text{ and } R_2 \text{ are regular expressions and } L(R_1) = L(R_2)\}$

where: p. 359

Description: The language of all pairs of regular expressions that generate the same language

Typ