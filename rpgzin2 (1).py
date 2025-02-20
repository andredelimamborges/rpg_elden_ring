import random
import time
from colorama import Fore, init

init(autoreset=True)

# ========== ASCII ART ==========
MALENIA_ASCII = f"""
{Fore.RED}                                                                           
                                              ++++++++++::                      
                                          ++++mm++::++--++++..                  
                              ::::--  ::++mmmm++::::@@++++::----                
                        ..mmMMmmMMmm::mmmmMM++::  mm..----##MM::mm              
                          ::++++MM::mmMMMM##..@@--MM::::mm..--..mm::            
                              MM++++##MMmmMM@@MM  --..----..++++  --....        
                ++::++++MM++    ++@@@@mmmm++mm::##@@++++MM######--MMMM--::      
          ::++++::mm++++MM++..MM..--++@@mm++mm@@  ..::MM##@@  MM@@--::mm::--..  
      mmMM@@--++@@MM::mm@@##MM::::----..MMMM::mm@@######....##::..++------      
  ::mm++++MM++--@@++::@@MM@@::--@@##----@@@@######@@::....--::::::--            
    ::::::MMmm::MM--MMmmmm##mm@@####--MM######MMmmMM::--::++--MM                
              ++::++MMmm++++::mm::  --@@@@MMMMMMmm++--##mm++                    
                        ..--++mm@@@@mm@@@@MMMM++##MMMMmmMM####MM                
                                mm@@##@@MM++##MMmmmmMM++########@@              
                              --@@@@@@mm##mmmm@@MMmm      mm######MM            
                              MMMM++--mmmmMM
                              ++::@@@@@@--::--::..##@@MM          
                              ..::::::--..mmMMmmmmmmMMMMmm++++        ++        
                                  ..----..  --mmmmMMmmmmmmmmMMmmmm              
                                                  mmmm::MMmm++::--++            
                                                    ....::::++++++--..          
                                                                                   
                                                  
       {Fore.WHITE}||| {Fore.RED}MALENIA, LÂMINA DE MIQUELLA {Fore.WHITE}|||
"""

ROT_KNIGHT_ASCII = f"""
{Fore.GREEN}
       ,/.
      // /-
     // /
  _,'/_/
  \\- , 
   \\  |  
    \\_|  
     _\\_
    '-.\\
"""

TARNISHED_ASCII = f"""
{Fore.YELLOW}
     ▄▄▄▄
    /   /\\
   /   / /
  /   / /
 /___/ /
 \\   \\/
  \\   \\
   \\___\\
"""

# ========== CLASSES ==========
class Tarnished:
    def __init__(self, nome, classe, vida, ataque, defesa, fp):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.vida_max = vida
        self.ataque = ataque
        self.defesa = defesa
        self.fp = fp
        self.fp_max = fp
        self.flask_charges = 2

    def atacar(self, inimigo):
        dano = random.randint(self.ataque -5, self.ataque +5)
        inimigo.vida -= dano
        print(f"\n{Fore.YELLOW}{self.nome} atacou {inimigo.nome} causando {dano} de dano!")
        time.sleep(1)

    def usar_flask(self):
        if self.flask_charges > 0:
            cura = int(self.vida_max * 0.3)
            self.vida = min(self.vida + cura, self.vida_max)
            self.flask_charges -= 1
            print(f"{Fore.GREEN}Você usou o Cálice de Lágrimas Carmesim! (+{cura} Vida)")
            print(f"{Fore.BLUE}Cargas restantes: {self.flask_charges}")
            time.sleep(1)
        else:
            print(f"{Fore.RED}Sem cargas do Cálice restantes!")

    def habilidade_especial(self, inimigo):
        if self.fp < 10:
            print(f"{Fore.RED}FP insuficiente! (Necessário: 10)")
            return False

        if self.classe == "Guerreiro":
            print(f"{Fore.CYAN}\n*** LÂMINA DA ORDEM DOURADA ***")
            dano = random.randint(self.ataque +5, self.ataque +15)
            inimigo.vida -= dano
            self.fp -= 10
        
        elif self.classe == "Feiticeiro":
            print(f"{Fore.BLUE}\n*** ESTRELA EXPLOSIVA ***")
            dano = random.randint(self.ataque +10, self.ataque +20)
            inimigo.vida -= dano
            self.fp -= 10
        
        elif self.classe == "Bandoleiro":
            print(f"{Fore.GREEN}\n*** DANÇA DAS LÂMINAS ***")
            for _ in range(3):
                dano = random.randint(self.ataque -3, self.ataque +3)
                inimigo.vida -= dano
                print(f"Golpe rápido: {dano}")
                time.sleep(0.3)
            self.fp -= 10
        
        print(f"FP restante: {self.fp}")
        time.sleep(1)
        return True

class Inimigo:
    def __init__(self, nome, vida, ataque, ascii_art):
        self.nome = nome
        self.vida = vida
        self.vida_max = vida
        self.ataque = ataque
        self.ascii_art = ascii_art

    def atacar(self, alvo):
        dano = random.randint(self.ataque -5, self.ataque +5)
        print(f"\n{Fore.RED}{self.nome} atacou {alvo.nome} causando {dano} de dano!")
        alvo.vida -= dano
        time.sleep(1)

class Malenia(Inimigo):
    def __init__(self, nome, vida, ataque, ascii_art):
        super().__init__(nome, vida, ataque, ascii_art)
        self.segunda_fase = False 

    def atacar(self, alvo):
        if self.vida <= self.vida_max * 0.5 and not self.segunda_fase:
            self.ativar_segunda_fase(alvo)
        else:
            super().atacar(alvo)

    def ativar_segunda_fase(self, alvo):
        self.segunda_fase = True
        self.vida = int(self.vida_max * 0.6)  
        self.ataque += 5  # Aumenta o ataque
        print(f"\n{Fore.MAGENTA}Malenia se transforma em sua forma verdadeira!")
        print(f"{Fore.RED}Eu sou Malenia, Deusa da Podridão. E agora, você conhecerá o verdadeiro desespero!")
        time.sleep(2)

    def ataque_especial(self, alvo):
        if self.segunda_fase:
            print(f"{Fore.MAGENTA}\nMALENIA CANALIZA: FLOR DA DESTRUIÇÃO!")
            time.sleep(1)
            print(f"{Fore.RED}Ela desencadeará um ataque devastador no próximo turno!")
            time.sleep(1)
            # No próximo turno, o ataque será executado
            dano = random.randint(40, 50)
            bloqueio = alvo.bloquear() if random.random() < 0.5 else 0
            dano_final = max(0, dano - bloqueio)
            alvo.vida -= dano_final
            print(f"{Fore.RED}Flor da Destruição causou {dano_final} de dano!")
            if hasattr(alvo, 'flask_charges') and alvo.flask_charges > 0:
                alvo.flask_charges -= 1
                print(f"{Fore.RED}Uma carga do seu Cálice foi consumida!")
        else:
            super().ataque_especial(alvo)

    def verificar_easter_egg(self, jogador):
        if jogador.nome.lower() == "yuki_6777" and self.vida <= self.vida_max * 0.2:
            print(f"\n{Fore.MAGENTA}Malenia cai de joelhos, surpresa:")
            print(f"{Fore.CYAN}''Você... Você é digno, {jogador.nome}...")
            print("Leve minha lâmina e minha lealdade!")
            print("Juntos encontraremos Miquella e queimaremos a Erdtree!''")
            self.vida = 0
            return True
        return False

# ========== FUNÇÕES DO JOGO ==========
def escolher_classe():
    nome = input(f"\n{Fore.YELLOW}Digite o nome do Maculado: ").strip()
    print(f"\n{Fore.YELLOW}Escolha sua classe:")
    print(f"{Fore.WHITE}1. Guerreiro - Vida: 130, Ataque: 25, Defesa: 20, FP: 30")
    print("2. Feiticeiro - Vida: 100, Ataque: 35, Defesa: 15, FP: 40")
    print("3. Bandoleiro - Vida: 115, Ataque: 30, Defesa: 18, FP: 35")
    
    while True:
        escolha = input("\nDigite o número da classe: ")
        if escolha == "1":
            return Tarnished(nome, "Guerreiro", 130, 25, 20, 30)
        elif escolha == "2":
            return Tarnished(nome, "Feiticeiro", 100, 35, 15, 40)
        elif escolha == "3":
            return Tarnished(nome, "Bandoleiro", 115, 30, 18, 35)
        else:
            print("Escolha inválida!")

def batalha(jogador, inimigo):
    print(f"\n{Fore.RED}===== {inimigo.nome} APARECEU! =====")
    print(inimigo.ascii_art)
    primeiro_turno = True
    
    while jogador.vida > 0 and inimigo.vida > 0:
        print(f"\n{Fore.GREEN}{jogador.nome} [Vida: {jogador.vida}/{jogador.vida_max} | FP: {jogador.fp}/{jogador.fp_max}]")
        print(f"{Fore.RED}{inimigo.nome} [Vida: {inimigo.vida}]")
        print(f"{Fore.WHITE}1. Atacar")
        print("2. Bloquear")
        print("3. Usar Cálice de Cura")
        print("4. Habilidade Especial (10 FP)")
        escolha = input("Escolha uma ação: ")

        if escolha == "1":
            jogador.atacar(inimigo)
        elif escolha == "2":
            bloqueio = random.randint(5, jogador.defesa)
            print(f"{Fore.CYAN}Bloqueio reduzindo {bloqueio} de dano!")
            dano_inimigo = max(0, random.randint(inimigo.ataque -5, inimigo.ataque +5) - bloqueio)
            jogador.vida -= dano_inimigo
            if dano_inimigo > 0:
                print(f"{Fore.RED}Dano recebido: {dano_inimigo}")
        elif escolha == "3":
            jogador.usar_flask()
        elif escolha == "4":
            if not jogador.habilidade_especial(inimigo):
                continue
        else:
            print("Ação inválida!")
            continue

        if inimigo.vida > 0:
            if isinstance(inimigo, Malenia):
                if primeiro_turno:
                    print(f"\n{Fore.RED}Malenia: {Fore.WHITE}Eu sou Malenia, Espada de Miquella.")
                    print(f"{Fore.RED}E eu nunca conheci a derrota, {jogador.nome}...")
                    primeiro_turno = False
                
                if inimigo.verificar_easter_egg(jogador):
                    break

                if random.random() < 0.25:
                    inimigo.ataque_especial(jogador)
                else:
                    inimigo.atacar(jogador)
            else:
                inimigo.atacar(jogador)

        if jogador.vida <= 0:
            if isinstance(inimigo, Malenia):
                print(f"\n{Fore.RED}Malenia: {Fore.WHITE}Que a vossa carne seja consumida. Pela podridão escarlate, {jogador.nome}...")
            else:
                print(f"\n{Fore.RED}VOCE FOI DERROTADO POR {inimigo.nome}...")
            return False
        elif inimigo.vida <= 0:
            print(f"\n{Fore.GREEN}VOCE DERROTOU {inimigo.nome}!")
            jogador.flask_charges = 2
            return True

# ========== JOGO PRINCIPAL ==========
def main():
    print(f"{Fore.YELLOW}\n=== ELDEN RING: A JORNADA DO MACULADO ===")
    print(TARNISHED_ASCII)
    
    jogador = escolher_classe()
    print(f"\n{Fore.YELLOW}Classe escolhida: {jogador.classe}")
    
    inimigo1 = Inimigo("Cavaleiro da Podridão", 70, 15, ROT_KNIGHT_ASCII)
    if not batalha(jogador, inimigo1):
        return
    
    print(f"\n{Fore.RED}\n===== PODRIDÃO SE INTENSIFICA... =====")
    inimigo2 = Inimigo("Cavaleiro Ascendido", 100, 20, ROT_KNIGHT_ASCII)
    if not batalha(jogador, inimigo2):
        return
    
    print(f"{Fore.MAGENTA}\n===== VOCÊ CHEGOU À RAÍZ DA PODRIDÃO =====")
    print(MALENIA_ASCII)
    time.sleep(2)
    malenia = Malenia("Malenia, Lâmina de Miquella", 180, 25, MALENIA_ASCII)
    malenia.vida_max = 180
    if batalha(jogador, malenia):
        print(f"{Fore.YELLOW}\n=== VOCÊ CONQUISTOU O CÍRCULO DE ELDEN RING! ===")

if __name__ == "__main__":
    main()
