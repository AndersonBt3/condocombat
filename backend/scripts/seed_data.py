"""Dados satíricos para seed do CondoCombat."""

from typing import Any

# ── Condomínios ────────────────────────────────────────────────────────

CONDOMINIOS: list[dict[str, Any]] = [
    {
        "nome": "Residencial Fofoca Feliz",
        "endereco": "Rua das Fuxicadas, 42 — Bairro do Mexerico",
        "cnpj": "12.345.678/0001-90",
        "telefone": "(11) 99999-8888",
        "email": "sindico@fofocafeliz.com.br",
    },
    {
        "nome": "Condomínio Barulho da Madruga",
        "endereco": "Avenida do Pancadão, 666 — Vila do Som",
        "cnpj": "98.765.432/0001-10",
        "telefone": "(11) 97777-6666",
        "email": "sindico@barulhodamadruga.com.br",
    },
    {
        "nome": "Edifício Disputa&Guerra",
        "endereco": "Travessa da Fofoca, 171 — Centro do Caos",
        "cnpj": "11.222.333/0001-44",
        "telefone": "(11) 95555-4444",
        "email": "sindico@disputaeguerra.com.br",
    },
]

# ── Apartamentos (3 condomínios × 5-6 aptos) ─────────────────────────

APARTAMENTOS: list[dict[str, Any]] = [
    # Residencial Fofoca Feliz (cond_id=1)
    {"numero": "101", "bloco": "A", "torre": "Principal", "condominio_idx": 0},
    {"numero": "102", "bloco": "A", "torre": "Principal", "condominio_idx": 0},
    {"numero": "201", "bloco": "B", "torre": "Secundária", "condominio_idx": 0},
    {"numero": "202", "bloco": "B", "torre": "Secundária", "condominio_idx": 0},
    {"numero": "301", "bloco": "C", "torre": "Garagem", "condominio_idx": 0},
    # Condomínio Barulho da Madruga (cond_id=2)
    {"numero": "01", "bloco": "Norte", "torre": "Torre do Som", "condominio_idx": 1},
    {"numero": "02", "bloco": "Norte", "torre": "Torre do Som", "condominio_idx": 1},
    {"numero": "03", "bloco": "Sul", "torre": "Torre da Paz", "condominio_idx": 1},
    {"numero": "04", "bloco": "Sul", "torre": "Torre da Paz", "condominio_idx": 1},
    {"numero": "05", "bloco": "Leste", "torre": "Torre do Fundão", "condominio_idx": 1},
    {"numero": "06", "bloco": "Leste", "torre": "Torre do Fundão", "condominio_idx": 1},
    # Edifício Disputa&Guerra (cond_id=3)
    {"numero": "1A", "bloco": "Bloco dos Apontamentos", "torre": None, "condominio_idx": 2},
    {"numero": "1B", "bloco": "Bloco dos Apontamentos", "torre": None, "condominio_idx": 2},
    {"numero": "2A", "bloco": "Bloco das Disputas", "torre": None, "condominio_idx": 2},
    {"numero": "2B", "bloco": "Bloco das Disputas", "torre": None, "condominio_idx": 2},
    {"numero": "3A", "bloco": "Bloco da Trégua", "torre": None, "condominio_idx": 2},
]

# ── Moradores (perfis cômicos) ───────────────────────────────────────

MORADORES: list[dict[str, Any]] = [
    # Residencial Fofoca Feliz (cond_idx=0)
    {
        "nome": "Dona Fofoqueira",
        "cpf": "111.111.111-11",
        "email": "fofoqueira@fofocafeliz.com",
        "telefone": "(11) 91111-1111",
        "tipo": "proprietario",
        "apartamento_idx": 0,
    },
    {
        "nome": "Seu Barriga",
        "cpf": "222.222.222-22",
        "email": "barriga@fofocafeliz.com",
        "telefone": "(11) 92222-2222",
        "tipo": "inquilino",
        "apartamento_idx": 0,
    },
    {
        "nome": "Maria Barulho",
        "cpf": "333.333.333-33",
        "email": "maria@fofocafeliz.com",
        "telefone": "(11) 93333-3333",
        "tipo": "proprietario",
        "apartamento_idx": 1,
    },
    {
        "nome": "João Reclamação",
        "cpf": "444.444.444-44",
        "email": "joao@fofocafeliz.com",
        "telefone": "(11) 94444-4444",
        "tipo": "sindico",
        "apartamento_idx": 2,
    },
    {
        "nome": "Tia do Andar de Cima",
        "cpf": "555.555.555-55",
        "email": "tia@fofocafeliz.com",
        "telefone": "(11) 95555-5555",
        "tipo": "proprietario",
        "apartamento_idx": 3,
    },
    # Condomínio Barulho da Madruga (cond_idx=1)
    {
        "nome": "DJ Paredão",
        "cpf": "666.666.666-66",
        "email": "dj@barulho.com",
        "telefone": "(11) 96666-6666",
        "tipo": "inquilino",
        "apartamento_idx": 5,
    },
    {
        "nome": "Madruguinha Silva",
        "cpf": "777.777.777-77",
        "email": "madruga@barulho.com",
        "telefone": "(11) 97777-7777",
        "tipo": "proprietario",
        "apartamento_idx": 6,
    },
    {
        "nome": "Seu Cochilo",
        "cpf": "888.888.888-88",
        "email": "cochilo@barulho.com",
        "telefone": "(11) 98888-8888",
        "tipo": "proprietario",
        "apartamento_idx": 7,
    },
    {
        "nome": "Dona Soneca",
        "cpf": "999.999.999-99",
        "email": "soneca@barulho.com",
        "telefone": "(11) 99999-9999",
        "tipo": "proprietario",
        "apartamento_idx": 8,
    },
    # Edifício Disputa&Guerra (cond_idx=2)
    {
        "nome": "Briguento Mendes",
        "cpf": "123.456.789-00",
        "email": "briguento@disputa.com",
        "telefone": "(11) 91234-5678",
        "tipo": "proprietario",
        "apartamento_idx": 11,
    },
    {
        "nome": "Paz & Amor Oliveira",
        "cpf": "987.654.321-00",
        "email": "paz@disputa.com",
        "telefone": "(11) 99876-5432",
        "tipo": "inquilino",
        "apartamento_idx": 12,
    },
    {
        "nome": "Advogado Chato Jr.",
        "cpf": "111.222.333-44",
        "email": "chato@disputa.com",
        "telefone": "(11) 91112-2233",
        "tipo": "proprietario",
        "apartamento_idx": 13,
    },
    {
        "nome": "Síndico Carrancudo",
        "cpf": "555.666.777-88",
        "email": "carrancudo@disputa.com",
        "telefone": "(11) 95556-6777",
        "tipo": "sindico",
        "apartamento_idx": 14,
    },
]

# ── Ocorrências ──────────────────────────────────────────────────────

OCORRENCIAS: list[dict[str, Any]] = [
    # Fofoca Feliz
    {
        "titulo": "Fofoca no elevador",
        "descricao": "Dona Fofoqueira foi flagrada contando que o morador do 102 está com o condomínio atrasado. Testemunhas confirmam.",
        "categoria": "outra",
        "gravidade": "media",
        "status": "aberta",
        "apartamento_idx": 0,
    },
    {
        "titulo": "Barulho ensurdecedor às 3h da manhã",
        "descricao": "Maria Barulho resolveu fazer uma festa para o gato dela. Vizinhos chamaram a polícia.",
        "categoria": "barulho",
        "gravidade": "alta",
        "status": "investigando",
        "apartamento_idx": 1,
    },
    {
        "titulo": "Briga por vaga de garagem",
        "descricao": "Seu Barriga estacionou na vaga do 201. Resultado: troca de ofensas e um retrovisor quebrado.",
        "categoria": "briga",
        "gravidade": "critica",
        "status": "aberta",
        "apartamento_idx": 0,
    },
    {
        "titulo": "Obra sem autorização",
        "descricao": "Tia do Andar de Cima resolveu quebrar a parede da sala num domingo de manhã. Marteladas ecoam por todo o prédio.",
        "categoria": "obra",
        "gravidade": "media",
        "status": "arquivada",
        "apartamento_idx": 3,
    },
    # Barulho da Madruga
    {
        "titulo": "Funk até o sol raiar",
        "descricao": "DJ Paredão resolveu testar o novo sistema de som às 2h da manhã. Seu Cochilo não dorme há 3 dias.",
        "categoria": "barulho",
        "gravidade": "alta",
        "status": "aberta",
        "apartamento_idx": 5,
    },
    {
        "titulo": "Animal solto no corredor",
        "descricao": "Madruguinha Silva deixou a porta aberta e o cachorro fugiu. O bichinho foi parar no apartamento da Dona Soneca e comeu o sofá dela.",
        "categoria": "animal",
        "gravidade": "media",
        "status": "resolvida",
        "apartamento_idx": 6,
    },
    {
        "titulo": "Festa na área comum",
        "descricao": "Um grupo de moradores resolveu fazer um churrasco na piscina às 23h. Cinco garrafas de vinho e uma caixa de som depois...",
        "categoria": "festa",
        "gravidade": "alta",
        "status": "investigando",
        "apartamento_idx": 8,
    },
    # Disputa&Guerra
    {
        "titulo": "Ofensas no grupo do condomínio",
        "descricao": "Briguento Mendes chamou Paz & Amor Oliveira de 'hipócrita' no grupo do WhatsApp. Prints foram anexados.",
        "categoria": "briga",
        "gravidade": "baixa",
        "status": "aberta",
        "apartamento_idx": 11,
    },
    {
        "titulo": "Reclamação de obra estrutural",
        "descricao": "Advogado Chato Jr. protocolou 14 páginas de reclamação sobre a reforma do hall de entrada. Alega que o tom do cinza não combina com o mármore.",
        "categoria": "obra",
        "gravidade": "media",
        "status": "aberta",
        "apartamento_idx": 13,
    },
    {
        "titulo": "Vazamento no teto do 1A",
        "descricao": "O apartamento 2A está com o banheiro vazando e caiu todo o gesso do teto do 1A. Advogado Chato Jr. já ameaça processar o condomínio.",
        "categoria": "outra",
        "gravidade": "alta",
        "status": "investigando",
        "apartamento_idx": 11,
    },
    {
        "titulo": "Discussão na assembleia",
        "descricao": "Assembleia ordinária terminou em briga generalizada após proposta de aumento de 5% no condomínio. Síndico Carrancudo perdeu a voz de tanto gritar.",
        "categoria": "briga",
        "gravidade": "critica",
        "status": "resolvida",
        "apartamento_idx": 14,
    },
    {
        "titulo": "Animal no jardim",
        "descricao": "Um gambá foi visto no jardim do condomínio. Paz & Amor Oliveira quer adotar. Briguento Mendes quer dedetizar.",
        "categoria": "animal",
        "gravidade": "baixa",
        "status": "aberta",
        "apartamento_idx": 12,
    },
]

# ── Rivalidades ───────────────────────────────────────────────────────

RIVALIDADES: list[dict[str, Any]] = [
    {
        "apartamento_a_idx": 0,  # Dona Fofoqueira (101 A)
        "apartamento_b_idx": 1,  # Maria Barulho (102 A)
        "motivo": "Fofoca sobre festa do gato às 3h da manhã",
        "nivel": "intenso",
    },
    {
        "apartamento_a_idx": 5,  # DJ Paredão (01 Norte)
        "apartamento_b_idx": 7,  # Seu Cochilo (03 Sul)
        "motivo": "Som alto todos os finais de semana",
        "nivel": "belico",
    },
    {
        "apartamento_a_idx": 11,  # Briguento Mendes (1A)
        "apartamento_b_idx": 12,  # Paz & Amor Oliveira (1B)
        "motivo": "Vizinhos de porta com visões opostas da vida",
        "nivel": "moderado",
    },
    {
        "apartamento_a_idx": 11,  # Briguento Mendes (1A)
        "apartamento_b_idx": 13,  # Advogado Chato Jr. (2A)
        "motivo": "Vazamento do banheiro que destruiu o teto",
        "nivel": "intenso",
    },
    {
        "apartamento_a_idx": 3,  # Tia do Andar de Cima (202 B)
        "apartamento_b_idx": 2,  # João Reclamação (201 B)
        "motivo": "Obra de domingo de manhã sem autorização",
        "nivel": "leve",
    },
]