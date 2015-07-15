oldfunc = self.func
batchSize = self.ctx.batchSize
def batched_func(split, iterator):
	return batched(oldfunc(split, iterator), batchSize)
func = batched_func