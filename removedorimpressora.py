import subprocess
import os

def listar_impressoras():
    try:
        resultado = subprocess.check_output(
            "wmic printer get name",
            shell=True
        ).decode("utf-8")

        linhas = resultado.split("\n")
        impressoras = []

        for linha in linhas:
            linha = linha.strip()
            if linha and linha.lower() != "name":
                impressoras.append(linha)

        return impressoras

    except Exception as e:
        print("Erro ao listar impressoras:", e)
        return []

def remover_impressora(nome):
    try:
        comando = f'wmic printer where name="{nome}" delete'
        subprocess.run(comando, shell=True, check=True)
        print(f"\n✔ Impressora '{nome}' removida com sucesso!")
    except subprocess.CalledProcessError:
        print("\n❌ Erro ao remover impressora. Execute como Administrador.")

def main():
    while True:
        os.system("cls")
        print("=========================================================")
        print("Desenvolvido Por Emanuel Costa - 2026")
        print("Removedor automático de Impressoras")
        print("=========================================================")

        impressoras = listar_impressoras()

        if not impressoras:
            print("\nNenhuma impressora encontrada.")
            input("\nPressione Enter para sair...")
            break

        print("\nSelecione a impressora que deseja remover:\n")

        for i, imp in enumerate(impressoras):
            print(f"{i+1} - {imp}")

        print("0 - Sair")

        try:
            escolha = int(input("\nDigite o número da opção: "))

            if escolha == 0:
                print("\nEncerrando o programa...")
                break

            if 1 <= escolha <= len(impressoras):
                confirmar = input(f"\nTem certeza que deseja remover '{impressoras[escolha-1]}'? (s/n): ")
                if confirmar.lower() == "s":
                    remover_impressora(impressoras[escolha-1])
                else:
                    print("Operação cancelada.")
            else:
                print("Opção inválida.")

        except ValueError:
            print("Digite apenas números.")

        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
