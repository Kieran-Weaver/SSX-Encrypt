#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <stdbool.h>
#include "pcg_variants.h"

uint64_t f(uint64_t s, uint64_t s2)
{
    // Read command-line options

    int rounds = 25;
    bool nondeterministic_seed = false;
    pcg64_random_t rng;
    pcg64_srandom_r(&rng, s, s2);
    for (int round = 1; round <= rounds; ++round) {

        for (int i = 0; i < 6; ++i) {
            pcg64_random_r(&rng);
        }
        pcg64_advance_r(&rng, -6);
        for (int i = 0; i < 6; ++i) {
            pcg64_random_r(&rng);
        }
    }

    return pcg64_random_r(&rng);
}
void stream_cipher(uint64_t * retval, uint64_t iv, uint64_t length_, uint64_t * key_blocks, uint64_t *plaintext_blocks){
    for (int i=0;i<length_;i++){
        retval[i] = plaintext_blocks[i] ^ f(iv^key_blocks[i],key_blocks[i]);
    }
}
int main(){
	int t = 1;
	printf("\nHow many hex blocks?\n");
	scanf("%d",&t);
	printf("%d",t);
    uint64_t *vals = (uint64_t *)(malloc((t+5)*sizeof(uint64_t)));
    uint64_t *vals2 = (uint64_t *)(malloc((t+5)*sizeof(uint64_t)));
	printf("\nEnter the message:\n");
	uint64_t ptext[t+2];
    uint64_t ktext[t+2];
	for (int i=0;i<t;i++){
		scanf("%lx",&ktext[i]);
	}
	printf("\nEnter the key:\n");
	for (int i=0;i<t;i++){
		scanf("%lx ",&ptext[i]);
	}
    stream_cipher(vals,0xdeadbeef,4,ptext,ktext);
    printf("\nEncrypted values:\n");
	for (int i=0;i<t;i++){
		printf("0x%lx \n",vals[i]);
	}
	stream_cipher(vals2,0xdeadbeef,4,ptext,vals);
    printf("\nDecrypted values:\n");
	for (int i=0;i<t;i++){
		printf("0x%lx \n",vals2[i]);
	}
    return 0;
}
