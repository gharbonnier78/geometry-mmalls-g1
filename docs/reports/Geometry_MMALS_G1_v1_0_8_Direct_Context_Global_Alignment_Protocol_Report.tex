\documentclass[11pt]{article}
\usepackage[margin=0.9in]{geometry}
\usepackage{booktabs,longtable,array,hyperref,xcolor,amsmath,amssymb,enumitem,microtype}
\usepackage[T1]{fontenc}
\hypersetup{colorlinks=true,linkcolor=blue,urlcolor=blue,citecolor=blue}
\setlist[itemize]{leftmargin=1.5em}
\setlist[enumerate]{leftmargin=1.7em}
\title{Geometry-MMALS G1 v1.0.8\\
Revised Direct Context Geometry and Global Fiber Alignment\\
Protocol and Archival Report}
\author{Guillaume Harbonnier}
\date{June 2026}

\newcommand{\Lc}{\mathcal{L}_{\mathrm{context}}}
\newcommand{\Lfar}{\mathcal{L}_{\mathrm{far}}}
\newcommand{\Lspread}{\mathcal{L}_{\mathrm{spread}}}
\newcommand{\Lfiber}{\mathcal{L}_{\mathrm{fiber}}}
\newcommand{\Lcentroid}{\mathcal{L}_{\mathrm{centroid}}}
\newcommand{\Lroute}{\mathcal{L}_{\mathrm{route}}}

\begin{document}
\maketitle

\begin{abstract}
Geometry-MMALS G1 v1.0.7 established that inferred context can support competitive and causally specific routing when direct sensory access is removed, but it exposed a geometry-objective mismatch: route regularization organized routes rather than context coordinates, and local source trajectories could improve while global centroid alignment degraded. This revised v1.0.8 protocol incorporates reviewer feedback by making the functional context scale-fixed, using a chord-compatible factor target, separating local geometry from anti-collapse and global alignment terms, and testing a focused ablation sequence at context dimension two with dimension four as a capacity probe. The same normalized context is used by the router, losses, metrics, and causal interventions. The report defines the mathematics, experimental contrasts, falsification criteria, archive boundary, and non-claims. It makes no C1--C6 empirical claim.
\end{abstract}

\section{Status inherited from v1.0.7}
The archived v1.0.7 seed-0 experiment supports three narrow development conclusions:
\begin{enumerate}
    \item direct sensory input created an architectural shortcut in the standard router;
    \item a forced context bottleneck remained operationally competitive and produced a specific, monotonic causal route response;
    \item route geometry improved under regularization, while context-space rank order did not improve significantly and global centroid alignment weakened.
\end{enumerate}
These findings reject the strong claim that context is intrinsically useless. They do not establish globally aligned functional geometry, predictive benefit from geometry, reproducible specialization, memory transport, or operational superiority.

\section{Central design problem}
The previous route objective constrained the route simplex:
\[
\Lroute \;:\; d_R(r_{s,a},r_{s,b}) \approx \tau(u_a,u_b),
\]
where $r_{s,a}$ is the route produced for source $s$ at factor value $u_a$. Priority A requires a constraint on the inferred context itself:
\[
\Lc \;:\; d_C(c_{s,a},c_{s,b}) \approx \tau(u_a,u_b).
\]
A direct Euclidean loss on unconstrained context vectors has a free scale. A network could stretch or compress the raw space without creating a comparable geometry across sources or runs. The revised protocol therefore defines a functional normalized context and uses it consistently throughout the context-mediated path.

\section{Functional context on the unit sphere}
Let the context encoder produce
\[
c^{\mathrm{raw}}_{s,a}\in\mathbb{R}^{d}.
\]
The functional context is
\begin{equation}
 c_{s,a}=
 \frac{c^{\mathrm{raw}}_{s,a}}
 {\max(\lVert c^{\mathrm{raw}}_{s,a}\rVert_2,\varepsilon)}.
 \label{eq:normalization}
\end{equation}
The same $c_{s,a}$ is used by:
\begin{itemize}
    \item the context-bottleneck router;
    \item local and global geometry losses;
    \item source-block and centroid metrics;
    \item held-out factor decoding;
    \item causal interventions.
\end{itemize}
The raw context remains in the trace only for audit diagnostics such as mean norm and norm dispersion. This prevents a model from satisfying the measured geometry with direction while routing through an unobserved magnitude channel.

\section{Chord-compatible factor geometry}
For unit vectors, half the Euclidean chord distance is
\begin{equation}
 d_C(c_{s,a},c_{s,b})=
 \frac{1}{2}\lVert c_{s,a}-c_{s,b}\rVert_2\in[0,1].
 \label{eq:halfchord}
\end{equation}
A linear target is not geometrically consistent with this spherical support. For the controlled interval $[-60^\circ,60^\circ]$, the full span $U_{\max}=120^\circ$ is mapped to a semicircle:
\begin{equation}
 \tau(u_a,u_b)=
 \sin\!\left[
 \frac{\pi}{2}
 \min\!\left(
 \frac{|u_a-u_b|}{U_{\max}},1
 \right)
 \right].
 \label{eq:target}
\end{equation}
Thus equal factors map to distance zero, intermediate gaps increase monotonically, and the two extremes map to opposite points on the unit sphere.

\section{Separated loss terms}
The revised protocol avoids hiding several scientific assumptions inside one scalar. Local geometry, far-pair separation, anti-collapse, fiber alignment, and centroid grounding are logged and weighted separately.

\subsection{Local same-source context matching}
For the set $P=\{(a,b):a<b\}$,
\begin{equation}
 \Lc=
 \mathbb{E}_{s}
 \frac{1}{|P|}
 \sum_{a<b}
 \left[
 d_C(c_{s,a},c_{s,b})-
 \tau(u_a,u_b)
 \right]^2.
 \label{eq:contextloss}
\end{equation}
This tests whether each source image follows a factor-ordered context trajectory. It does not by itself require different source images to share one orientation.

\subsection{Far-pair separation}
Let $U_{\mathrm{far}}=60^\circ$ and $m_{\mathrm{far}}$ be the minimum half-chord distance for far pairs:
\begin{equation}
 \Lfar=
 \mathbb{E}_{s,a<b:\,|u_a-u_b|\geq U_{\mathrm{far}}}
 \left[
 \max\!\left(0,m_{\mathrm{far}}-d_C(c_{s,a},c_{s,b})\right)
 \right]^2.
 \label{eq:farloss}
\end{equation}
The matching loss already penalizes a complete point collapse when factor targets are nonzero. The far margin specifically guards against an overly compressed trajectory that compromises between several targets.

\subsection{Per-source path spread}
For $A$ factor views of source $s$ and $\bar c_s=A^{-1}\sum_a c_{s,a}$,
\begin{equation}
 \Lspread=
 \mathbb{E}_{s}
 \left[
 \max\!\left(
 0,
 v_{\min}-
 \frac{1}{A}\sum_a
 \lVert c_{s,a}-\bar c_s\rVert_2^2
 \right)
 \right]^2.
 \label{eq:spreadloss}
\end{equation}
This term is scale invariant because it acts on normalized contexts. Its weight is explicit, so anti-collapse pressure can be audited independently from factor matching.

\subsection{Interval-wise fiber alignment}
Sort the factor values and define adjacent displacements
\[
 \Delta c_{s,a}=c_{s,a+1}-c_{s,a},
 \qquad
 \widehat{\Delta c}_{s,a}=\frac{\Delta c_{s,a}}{\lVert\Delta c_{s,a}\rVert_2}.
\]
For each transition $a\rightarrow a+1$, let
\[
 \widehat{\overline{\Delta c}}_a=
 \frac{\sum_s\widehat{\Delta c}_{s,a}}
 {\left\lVert\sum_s\widehat{\Delta c}_{s,a}\right\rVert_2}.
\]
The alignment loss is
\begin{equation}
 \Lfiber=
 \frac{1}{A-1}\sum_a
 \frac{1}{S}\sum_s
 \left[
 1-\left\langle
 \widehat{\Delta c}_{s,a},
 \widehat{\overline{\Delta c}}_a
 \right\rangle
 \right].
 \label{eq:fiberloss}
\end{equation}
Tangents are aligned transition by transition. A curved trajectory is not forced to share one global tangent at all factor values. A weak transition-length consistency term is reported separately inside this component.

\subsection{Factor-centroid grounding}
For factor-level centroids
\[
 \mu_a=\operatorname{normalize}\!\left(\frac{1}{S}\sum_s c_{s,a}\right),
\]
$\Lcentroid$ applies Equations~\eqref{eq:halfchord}--\eqref{eq:contextloss} to $\mu_a$. This separates the question of local source order from the stronger question of a shared global coordinate orientation.

\subsection{Total objective}
The complete objective is
\begin{align}
 \mathcal{L}={}&
 \mathcal{L}_{\mathrm{CE}}
 +\lambda_{\mathrm{anchor}}\mathcal{L}_{\mathrm{anchor}}
 +\lambda_r\Lroute
 +\lambda_c\Lc
 +\lambda_f\Lfar \\
 &+\lambda_v\Lspread
 +\lambda_a\Lfiber
 +\lambda_g\Lcentroid
 +\lambda_h\mathcal{L}_{\mathrm{host-div}}.
 \label{eq:total}
\end{align}
The implementation logs every component, path variance, fiber resultant length, near/far context distances, and raw context norm.

\section{Ablation design}
The primary experiment uses context dimension two, preserving the minimal context hypothesis while adding explicit anti-collapse control. Dimension four is a separate capacity probe.

\begin{center}
\begin{tabular}{lccccc}
\toprule
Variant & Route & Context & Spread & Fiber & Centroid \\
\midrule
No geometry & 0 & 0 & 0 & 0 & 0 \\
Route only & yes & 0 & 0 & 0 & 0 \\
Context only & 0 & yes & yes & 0 & 0 \\
Route + context & yes & yes & yes & 0 & 0 \\
Full alignment & yes & yes & yes & yes & yes \\
Full alignment, $d=4$ & yes & yes & yes & yes & yes \\
\bottomrule
\end{tabular}
\end{center}

All methods of the same dimension share initialization, source order, image-forward count, optimizer-step count, frozen sensory grove, host architecture, anchor weight, and curriculum. The $d=4$ comparison is not interpreted as a parameter-matched causal effect.

\section{Evidence outputs}
The notebook exports the following evidence families.

\subsection{Local and global geometry}
For trained, interpolation, and extrapolation partitions separately:
\begin{itemize}
    \item source-block Spearman distance-order correlation;
    \item source-block normalized stress;
    \item factor-centroid correlation and stress;
    \item fiber resultant length for each transition;
    \item held-out-source ridge factor decoding.
\end{itemize}
Treatment-control deltas are paired by source image and bootstrapped over source identities. Both correlation and stress deltas are exported.

\subsection{Anti-collapse diagnostics}
The report includes:
\begin{itemize}
    \item mean and minimum per-source path variance;
    \item effective covariance rank of normalized context;
    \item mean raw-context norm and norm dispersion;
    \item near and far half-chord distances;
    \item far-to-near distance ratio.
\end{itemize}
A high geometric score is not accepted if the representation has collapsed effective rank or negligible path variance.

\subsection{Functional and causal controls}
Accuracy, NLL, forgetting, interpolation performance, route geometry, and static evidence remain visible. The causal tangent is fitted on one source subset and evaluated on disjoint source identities. Because context lies on a sphere, interventions are projected into the local tangent plane and renormalized. Orthogonal causal controls are interpreted primarily in dimension four; the unit circle has only one intrinsic tangent direction.

\section{Decision criteria}
\subsection{Local context-geometry candidate}
A candidate local result requires
\[
 \Delta\rho_{\mathrm{context,source}}>0
\]
with a strictly positive paired-bootstrap lower bound, together with
\[
 \Delta\operatorname{stress}_{\mathrm{context,source}}<0.
\]

\subsection{Global alignment candidate}
A global candidate requires convergent improvement in:
\begin{itemize}
    \item context factor-centroid order;
    \item fiber resultant length;
    \item held-out-source factor decoding;
    \item non-collapse diagnostics.
\end{itemize}
Local source order alone is insufficient.

\subsection{Functional usefulness}
Even a positive C1 candidate does not imply utility. Accuracy, NLL, forgetting, interpolation, causal specificity, and static-route comparisons must continue to be reported. Geometry without operational improvement remains a representational result only.

\section{Interpretation matrix}
\begin{longtable}{p{0.39\textwidth}p{0.53\textwidth}}
\toprule
Observed result & Interpretation \\
\midrule
Context-only loss improves source $\rho$ and stress & Direct local supervision is effective. \\
Local order improves but centroid order remains flat & Source fibers remain independently rotated or reflected. \\
Full alignment improves centroid order and resultant length & A shared global orientation is emerging. \\
Context improves while route degrades, or conversely & Context and route objectives impose incompatible geometries. \\
Path variance or effective rank collapses & Anti-collapse pressure or context capacity is inadequate. \\
Dimension four succeeds where dimension two fails & Capacity/topology limitation; not a clean treatment effect. \\
Geometry improves without prediction & C1 evidence only; no C6 operational claim. \\
No geometric effect in either dimension & Reconsider the context encoder, supervision target, or factor topology. \\
\bottomrule
\end{longtable}

\section{Archive and reviewer materials}
The GitHub package includes:
\begin{itemize}
    \item the revised v1.0.8 Colab notebook;
    \item source implementations and tests for normalized context geometry;
    \item the complete executed v1.0.7 seed-0 result bundle;
    \item the 22-page Status and Perspective reviewer report v1.1;
    \item the complete reviewer-report LaTeX source and figures;
    \item this protocol report and its LaTeX source;
    \item version history, tracked changes, release checks, and manifests.
\end{itemize}
Datasets, Git internals, bytecode, caches, and local environments are excluded from the clean release package.

\section{Claim boundary and perspective}
Version 1.0.8 is a falsifiable protocol release. It does not claim C1--C6 qualification, globally aligned context geometry, predictive benefit, causal qualification, host specialization, backward transfer, memory transport, domain generalization, or quantum advantage.

If local context order succeeds but global alignment fails, the model should be treated as a bundle of source-conditioned fibers rather than one global manifold. If full alignment succeeds, the next justified step is a frozen multi-seed G1 qualification. If neither direct supervision nor dimension four helps, the present definition of inferred context must be reconsidered before G2 energy-guided routing or G3 phase-aware extensions.

\appendix
\section{Tracked revision items}
The reviewer-loss-design revision adds fifteen explicit tracked changes: normalized functional routing, raw-context audit traces, chord targets, far separation, path spread, interval-wise fiber alignment, separate centroid grounding, focused ablations, a dimension-four capacity probe, collapse diagnostics, paired stress deltas, spherical causal interventions, preserved v1.0.7 evidence, retained reviewer materials, and strict C0-only claim status.

\end{document}
