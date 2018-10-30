#!/usr/bin/env bash

# Environment variables
BLOCKCHAIN_NAME = $(cat setup/reference/black/blockchain_name.txt)


# Initialize parameters
#multichain-util create $BLOCKCHAIN_NAME

# Create blockchain
#multichaind $BLOCKCHAIN_NAME -daemon

echo $BLOCKCHAIN_NAME
