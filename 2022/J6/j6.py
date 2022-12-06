def isStrictlyDifferent(list):
    return len(list) == len(set(list))

with open('./input.txt', 'r') as communication:
    radio_flux = communication.readlines()[0]

    chunck_size = 13

    for iteration in range(chunck_size, len(radio_flux)):
        chunck = radio_flux[slice(iteration-chunck_size, iteration+1)]
        if(isStrictlyDifferent(chunck)):
            print("Response is {}".format(iteration+1))
            break
