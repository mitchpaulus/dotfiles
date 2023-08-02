    ! asdf
    REAL FUNCTION ZERO(A, B, MACHEP, T, F)
    REAL A, B, MACHEP, T, F, SA, SB, C, D, E, FA, FB, FC, TOL, M, P, Q, R, S
    SA = A
    SB = B
    FA = F(SA)
    FB = F(SB)
10  C = SA
    FC = FA
    E = SB - SA
    D = E
20  IF (ABS(FC) .GT. ABS(FB)) GO TO 30
    SA = SB
    SB = C
    C = SA
    FA = FB
    FB = FC
    FC = FA
30  TOL = 2.0*MACHEP*ABS(SB) + T
    M = 0.5*(C-SB)
    IF ((ABS(M) .LE. TOL) .OR. (FB .EQ. 0.0)) GO TO 140
    IF ((ABS(E) .GE. TOL) .AND. (ABS(FA) .GT. ABS(FB))) GO TO 40
    E = M
    D = E
    GO TO 100
40  S = FB/FA
    IF (SA .NE. C) GO TO 50
    P = 2.0*M*S
    Q = 1.0 - S
    GO TO 60
50  Q = FA/FC
    R = FB/FC
    P = S*(2.0*M*Q*(Q-R)-(SB-SA)*(R-1.0))
    Q = (Q-1.0)*(R-1.0)*(S-1.0)
60  IF (P .LE. 0.0) GO TO 70
    Q = -Q
    GO TO 80
70  P = -P
80  S = E
    E = D
    IF ((2.0*P .GE. 3.0 * M*Q - ABS(TOL*Q)) .OR. (P .GE. ABS(0.5 * S * Q))) GO TO 90
    D = P/Q
    GO TO 100
90  E = M
    D = E
100 SA = SB
    FA = FB
    IF (ABS(D) .LE. TOL) GO TO 110
    SB = SB + D
    GO TO 130
110 IF (M .LE. 0.0) GO TO 120
    SB = SB + TOL
    GO TO 130
120 SB = SB - TOL
130 FB = F(SB)
    IF ((FB .GT. 0.0 .AND. FC .GT. 0.0) .OR. (FB .LT. 0.0 .AND. FC .LT. 0.0)) GO TO 10
    GO TO 20
140 ZERO = SB
    RETURN
    END
