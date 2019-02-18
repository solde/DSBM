# DSBM

## Introducció

Poca cosa

## Embedded System

- Funció espedífica
- Part d'un sistema més ampli
- Basats en micros
- Hadware limitat
- Qualitat i fiabilitat elevats
- Adequat per sistemes a temps real

## Repàs de conceptes electrònics

### Generadors

- Generació de tensió alterna
    - Xarxa elèctrica, dinamo
- Generació de tensió continua
    - Bateries, piles, cel·les fotoelèctriques, fonts d'alimentació...

### Conductors i aïllants

Conductor: material que oposa pocs resitència al pas de corrent

Aïllant: material que s'oposa al pas de la corrent

Semiconductors: material que està entre conductors i aïllants i que permet controlar la conductivitat mitjançant l'adició dimpreses p(+) i N(-)

### Dispositius passius

- Resistències

    $R = \frac{Va - Vb}{I}$

- Condensadors

    $I_c = C \frac{dv_c}{dt}$; $V_c = \frac{1}{C} \int I_c dt$

    - S'oposa a canvis ràpids de la tensió
    - Subministra corrent sense variar al sensivilitat
    - La impedància disminueix en funció de la freqüència

- Inductàncies

    $V_l = -L \frac{dI_l}{dt}$: $I_c = \frac{1}{L} \int V_l dt$

    - S'oposa als canvis ràpids de corrent
    - Subministra pics de tensio
    - La impedància augmenta en funció de la freqüència

### Lleis de kirchoff

- Malla: Elemets d'un circuit connectats formant un llaç tencat.

    $\sum_0^nV_i = 0 \Rightarrow V_{cc} = V_1 + V_2 + V_3 + ... V_n$

- Node: punt d'un circuit on es connecten dos o més elements

    $\sum_0^nI_i = 0 \Rightarrow I_{in} = I_{out}$

### Ciucuit RC

Composat per un generador i una Resistència.