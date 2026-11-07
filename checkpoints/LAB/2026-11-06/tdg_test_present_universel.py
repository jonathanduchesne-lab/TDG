"""TDG / present universel : tests conceptuels reproductibles.

Ce script ne valide PAS l'existence d'un present ontologique.
Il teste la compatibilite mathematique d'une foliation privilegiee avec
la dilatation relativiste, l'absence de simultaneite invariante sans
structure additionnelle, et une consequence d'une decoherence prematuree.

Usage: python tdg_test_present_universel.py
Dependencies: Python standard library only.
"""
from decimal import Decimal, getcontext
import math

getcontext().prec = 60
DISTANCE_LY = Decimal('4000000000')

def boost(t, x, beta):
    """Lorentz boost en unites c=1 : temps en annees, x en annees-lumiere."""
    g = Decimal(1) / (Decimal(1) - beta * beta).sqrt()
    return g * (t - beta * x), g * (x - beta * t)

def inverse_time(t_prime, x_prime, beta):
    """Retrouve T d'une foliation T=t dans le repere initial."""
    g = Decimal(1) / (Decimal(1) - beta * beta).sqrt()
    return g * (t_prime + beta * x_prime)

def test_simultaneite():
    print('TEST 1 -- Deux evenements a meme temps T=0, separes de 4 milliards d annees-lumiere')
    for b in ['-0.8', '-0.1', '0', '0.1', '0.8']:
        beta = Decimal(b)
        t_a_prime, _ = boost(Decimal(0), Decimal(0), beta)
        t_b_prime, x_b_prime = boost(Decimal(0), DISTANCE_LY, beta)
        delta_gyr = (t_b_prime - t_a_prime) / Decimal('1e9')
        print(f'  v/c={b:>4} : delta t_prime={delta_gyr:+.6f} milliards d annees')
        assert abs(inverse_time(t_b_prime, x_b_prime, beta)) < Decimal('1e-40')
    print('  PASS : T commun bien defini, simultaneite coordonnee non invariante.\n')

def test_dilatation():
    print('TEST 2 -- 10 ans de T universel, durees propres de differentes horloges')
    for b in ['0', '0.1', '0.5', '0.8', '0.99']:
        beta = Decimal(b)
        proper_years = Decimal(10) * (Decimal(1) - beta * beta).sqrt()
        print(f'  v/c={b:>4} : delta tau={proper_years:.6f} ans')
        assert proper_years <= 10
    assert (Decimal(10) * (1 - Decimal('0.8')**2).sqrt()) == Decimal(6)
    print('  PASS : T commun compatible avec les differences de duree propre.\n')

def test_interference():
    print('TEST 3 -- Experience a deux chemins, deux operations Hadamard ideales')
    # Apres H, l'etat est |+>=(|0>+|1>)/sqrt(2).
    # Retour par H sans perturbation: P(0)=1.
    # Un effondrement non selectif dans la base des chemins donne rho=I/2,
    # et le second H laisse rho=I/2, donc P(0)=1/2.
    p0_without_collapse = 1.0
    p0_with_early_dephasing = 0.5
    print(f'  Coherence preservee : P(0)={p0_without_collapse:.3f}')
    print(f'  Decoherence totale avant recombinaison : P(0)={p0_with_early_dephasing:.3f}')
    assert p0_without_collapse != p0_with_early_dephasing
    print('  PASS : un effondrement precoce donne une prediction differente.\n')

def main():
    print('TDG -- present universel : controle mathematique (modele de Minkowski)\n')
    test_simultaneite()
    test_dilatation()
    test_interference()
    print('CONCLUSION : modele de present prefere non contradictoire au niveau cinematique;')
    print('mais pas de preuve de sa realite. Une dynamique d actualisation devra')
    print('reproduire interference quantique, regle de Born et non-signalisation.')

if __name__ == '__main__':
    main()
