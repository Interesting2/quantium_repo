#!/bin/bash

source venv/bin/activate

pytest

exit_code=$?

# Define colors
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

if [[ "$exit_code" -eq 0 ]]; then
    echo -e "${GREEN}✅ All tests passed successfully!${NC}"

    exit 0
else
    echo -e "${RED}❌ Some tests failed!${NC}"

    exit 1
fi