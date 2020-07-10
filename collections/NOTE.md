学习笔记
## chainMap:
1. dict-like class for creating a single view of multiple mappings
2. ChainMap(adjustment,baseline): 用adjustment 去调节 baseline
3. The ChainMap class only makes updates (writes and deletions) to the first mapping in the chain 
4. while lookups will search the full chain. 
5. if deep writes and deletions are desired, it is easy to make a subclass that updates keys found deeper in the chain
    - deepChainMap.py