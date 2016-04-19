package com.senghuotlim.cci;

public class BitVector {
	
	int[] vectors;
	public BitVector(int size) {
		vectors = new int[size / 32];
	}
	
	public boolean getBit(int position) {
		int vector = vectors[position / 32];
		int index = position % 32;
		return (vector & (0x1 << index)) != 0;
	}
	
	public void setBit(int position) {
		int index = position % 32;
		vectors[position / 32] |= 1 << index;
	}
}