import wandb
wandb.init(settings=wandb.Settings(start_method="fork"))

for x in range(10):
    run = wandb.init(reinit=True)
    for y in range (100):
        wandb.log({"metric": x+y})
    run.finish()