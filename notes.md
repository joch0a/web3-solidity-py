Course: https://www.youtube.com/watch?v=M576WGiDBdQ&ab_channel=freeCodeCamp.org

Current minute: https://www.youtube.com/watch?v=M576WGiDBdQ&ab_channel=freeCodeCamp.org

Raw english/spanish notes to myself lol :)

# Lesson 0:

## Core concepts

### Decentralized (No single point of authority)
### Transparency & Flexibility
### Speed and efficiency
### Security and inmmutability - Cannot be corrupted. 
### Removal of counterparty risk
### Trust minized agreements
### Hybrid smart contrats combine on and off-chains

---

Hacer una transaccion en eth

Se necesita una wallet - MetaMask

Etherscan - Scan accounts 

Testnets are free for testing
Mainnet cost money and are considered "live"

Testear con rinkeby - faucet.rinkeby.io
https://rinkeby.etherscan.io/

Faucet: App that give free test tokens.
Block explorer: app that allows to view transactions on the blockchain (etherscan)

Gas: Unit of computational measure. The more computation a transaction uses the more "gas" you have to pay. Every transaction that happens on-chain pays a "gas fee" to node operators. (Prob will change in the future)

Gas: Measure of computational use
Gas price: How much it costs per unit of gas
Gas Limit: Max amount of gas in a transaction

Transaction fee: Gas used * Gas price

ie
21000 gas @ 1 GWEI per gas = 21000 GWEI

Porque se puede especificar el Gas price? Porque hay muchas operaciones que se estan realizando en el momento y esto permite priorizar nuestra transaccion. www.ethgasstation.info permite ver precios aproximados del momento para saber el valor en GWEI dependiendo que tan rapido queremos realizar la operacion.

Direccion:

0x29F019590900f135B0A6D0F19b65b6379E18e2D6

------------------------------------------------------

Blockchain fundamentals: https://youtu.be/M576WGiDBdQ?t=2649

Hash: unique fixed length string meant to identify a piece of data.
Keccak256 - used by ETH

------------------------------------------------------

Minar = encontrar el nonce tal que el hash de la data genere 4 ceros al principio (Al menos en el ejemplo). Buscar el nonce que resuelva algun problema.

------------------------------------------------------

Block:
    - Block number
    - Nonce (Solution number, sometimes used as transaction number)
    - Data (Tx) Transacciones que se hicieron en ese bloque.
    - Hash

BlockChain:
    - Same as block + prev hash.

Inmutable por el hecho de que si cambias un solo bloque, se invalida toda la blockchain.

Si soy el owner de la blockchain, podria modificar los datos del pasado y re-minar todo pero aca es donde entra en juego el hecho del que la blockchain sea distribuida. Los peers comparan sus hashes y cuando hay uno que se diferencia lo echan de la blockchain.


------------------------------------------------------
Como sabemos el from/to correctamente?

Public y private keyss.

Algoritmo usado para generar las public key (Elliptic Curve digital signature algorithm)

Se firma con las private keys, se validan con las public keys.

------------------------------------------------------

Proof of work > Consensus > Forma de estar de acuerdo entre los pares

- Chain selection ->
- Sybil resistance -> Forma

Proof of work -> Ver la forma de saber quien es el creador del nodo ->  Sybil resistance -> Encontrar el nonce permite que aun teniendo muchos nodos hay que competir.


Nakamoto consensus -> La chain que es la original -> La block que tiene mas nodo

Block confirmations -> 

Sybil attack - A lot of anom accounts to get influence. Se mitiga con PoW&PoS
51% attack - Tener el 51% de los votos para poder modificar la blockchain. Mientras mas grande es la blockchain, mas segura es.

PoW  -> uses a lot of energy

Proof of stake -> Not mining/Validators -> Se elige un nodo para proponer el siguiente bloque. Si los validadores lo aprueban va a la blockchain. Si se ve que un nodo esta comportandose de forma maligna se lo castiga pudiendo resultar en grandes perdidas de capital
Usa mucho menos energia. 
Puede argumentarse que no es lo sufieciente de-centralizado.

Scalability:
    - Sharding: Blockchain of blockchains.
    - Rollups: Rollups perform transaction execution outside layer 1 and then the data is posted to layer 1 where consensus is reached.

- Layer 1: Base layer blockchain implementation
- Layer 2: Any app built on top of a layer 1

# Lesson 1: Simple storage


Define Solidity version =>0.6.0 <0.9.0

Define a contract -> class in java

Types and variables: https://docs.soliditylang.org/en/v0.8.11/types.html

View & pure -> do not modify state.
pure -> do some math but not modify state

struct -> way to create new objects

memory vs storage

Memory -> se guardan solo en execucion
Storage -> se queda dsp de la execucion

Add SPDX License Identifier


# Lesson 1: Storage Factory