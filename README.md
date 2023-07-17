# 4th_year_report_assignment
４年生のレポート（tex）
途中からのため２つだけ
色々問題点があるので信用しないように

図１より垂直方向の力のつり合いと B 点に関するモーメントのつり合いから,
\begin{equation} 
  R_A+R_B=W,R_al-W(l-a)=0
\end{equation}
となり,これから
\begin{equation} 
  R_A={\dfrac{l-a}{l}W},R_B={\dfrac{a}{l}W}
\end{equation}
を得る．$x$断面における曲げモーメントは,AC 側と CB 側とでは,
\begin{equation} 
  M_{AC}=R_Ax={\dfrac{W(l-a)}{l}x},M_{CB}=R_Ax-W(x-a)={\dfrac{Wa}{l}(l-x)}
\end{equation}
となる．したがって,たわみの基本式より
\begin{equation} 
  {(\dfrac{d^2y}{dx^2})_{AC}}={-\dfrac{W(l-a)}{EIl}x},
  {(\dfrac{d^2y}{dx^2})_{CB}}={-\dfrac{Wa}{EIl}(l-x)}
\end{equation}
となる．これを積分すれば
\begin{equation} 
  {(\dfrac{dy}{dx})_{AC}}={-\dfrac{W(l-a)}{2EIl}x^2+c_1},
  {(y)_{AC}}={-\dfrac{W(l-a)}{6EIl}x^3+c_1x+c_2}
\end{equation}
