def calculate_summ(randomcpu, randomram, randommemory1):
    const_cpu_1 = 0.025
    const_sata_10 = 10 * 0.000192
    const_ip_1 = 0.00625
    const_ram_1 = 0.0125

    cpu = const_cpu_1 * int(randomcpu)
    ram = const_ram_1 * int(randomram)
    sata = const_sata_10 * (int(randommemory1) * 0.1)

    summ = cpu + ram + sata + const_ip_1
    summa = summ * 730

    return round(summa)

