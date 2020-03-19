
#Stap1 importeer de dependencies:
#genereert de timestamps 
import datetime
#bevat de hashing algoritmes
import hashlib

#Stap2 Creeer een Block

#definieer de 'block' data structuur
class Block:
    #ieder block heeft 7 attributes 
  
    #1 nummmer van het block
    blockNo = 0
    #2 welke data is opgeslagen in dit block?
    data = None
    #3 pointer naar het volgende block
    next = None
    #4 De hash van dit block (dient als een unique ID en verifieert z'n integriteit)
    #Een hash is een functie die data converteert in een nummer binnen een bepaalde range. 
    hash = None
    #5 Een nonce is een nummer wat slechts een keer wordt gebruiikt (number only used once) 
    nonce = 0
    #6 Sla de hash (ID)op van het vorige block in de chain
    previous_hash = 0x0
    #7 timestamp 
    timestamp = datetime.datetime.now()

    #We initialiseren een block door er wat data in op te slaan
    def __init__(self, data):
        self.data = data

    #Functie om de 'hash' van een  block te berekenen
    #een hash dient ervoor om zowel een unieke identiteit te creeen
    #als de integriteit te waarborgen
    #als iemand de hash van een block wijzigt
    #dan wordt ieder block wat daarna komt,gewijzigd
    #dit helpt om de blockchain immutable te maken
    def hash(self):
        #SHA-256 is een hashing algoritme dat
        # geen bijna unieke 256-bit handtekening genereert die een
        # stuk tekst vertegenwoordigt
        h = hashlib.sha256()
        #de input in het SHA-256 algoritme
        #zal een  concatenated string zijn 
        #bestaande uit 5 block attributes
        #the nonce, data, previous hash, timestamp, & block #
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        #returns een hexademicale string
        return h.hexdigest()
      
      # verander de data 

    def __str__(self):
        #print de waarde van een block 
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"

#Stap3 Creeer een Blockchain

    #definieer de blockchain datastructuur
    #consists uit 'blocks' die samen gelinkt zijn
    #om een 'chain'.te vormen Dat is waarom het een 
    #'blockchain' wordt genoemd 
    
class Blockchain:
    
    #mining moeilijkheidsgraad
    diff = 20
    #2^32. Dit is het maximum nummer
    #die we in een 32-bit nummer kunnen opslaan
    maxNonce = 2**32
    #target hash, voor mining
    target = 2 ** (256-diff)

    #genereert het eerste blok in de blockchain
    #dit wordt het 'genesis block' genoemd
    block = Block("Genesis")
    #set de kop van onze blockchain
    head = block

    #voegt een gegeven block toe aan de chain van blocks
    #het block wat wordt toegevoegd is de enige parameter
    def add(self, block):
        
        #set de hash van een vorig block
        #als ons nieuwe block's vorige hash
        block.previous_hash = self.block.hash()
        #set de block # van ons nieuwe block
        #als het gegeven block's # + 1, omdat
        #het de volgende in de chain is
        block.blockNo = self.block.blockNo + 1

        #set het volgende block gelijk aan 
        #zichzelf. Dit is de nieuwe kop(head) 
        #van de blockchain
        self.block.next = block
        self.block = self.block.next

    #Bepaalt of we wel of niet een gegeven block aan
    #de blockchain kunnen toevoegen
    def mine(self, block):
        #van 0 to 2^32 
        for n in range(self.maxNonce):
            #is de waarde van een gegeven block's hash minder dan onze target waarde?
            if int(block.hash(), 16) <= self.target:
                #als dat zo is,
                #voeg een block toe aan de chain
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1
   
 #Mine een block

#initialiseer de blockchain



blockchain = Blockchain()

#Stap4 Priint de Blockchain uit

#mine 10 blocks
for n in range(10):
    blockchain.mine(Block("Block " + str(n+1)))
    
#print ieder block in de blockchain uit
while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next