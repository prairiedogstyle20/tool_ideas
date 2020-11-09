#include "main.hpp"
#include <stdio.h>
#include <iostream>
#include <string>
#include <array>

/*
 * Spamcheck is only being designed for use with EXIM as the MTA running on cPanel server
 * This should allow for easily finding the spamming account based on analysing the return
 * status in logs as well as providing a full report on the emal that is being delivered by
 * each email account on the server. 
 */


int main(int argc, char *argvp[]){
    printf( "hello there\n");
    return(0);
}
