CXX=g++
CFLAGS=-std=gnu++11

spamcheck: main.o 
	$(CXX) $(CFLAGS) -o spamcheck main.o

main.o: main.cpp main.hpp
	$(CXX) $(CFLAGS) -c main.cpp

clean:
	$(RM) spamcheck
