from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class MatriculaAnonRateThrottle(AnonRateThrottle):
    rate = '5/day'
    # altera em específico o login de usuário anônimo, limitando 5 acessos por dia 