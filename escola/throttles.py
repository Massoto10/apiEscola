from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class MatriculaAnonRateThrottle(AnonRateThrottle):
    rate = '5/day'
    # crio essa clase para alterar em específico o login de usuário anônimo, limitando 5 acessos por dia 