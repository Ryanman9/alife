import time

from simulation.world import World


def main():
    world = World(width=40, height=10, n_creatures=40)
    print("---- Creature trait distribution ----")
    speeds = [c.speed for c in world.creatures]
    visions = [c.vision for c in world.creatures]

    print(
        f"Speed  — min: {min(speeds):.2f}, max: {max(speeds):.2f}, "
        f"avg: {sum(speeds) / len(speeds):.2f}"
    )
    print(
        f"Vision — min: {min(visions):.2f}, max: {max(visions):.2f}, "
        f"avg: {sum(visions) / len(visions):.2f}"
    )

    for i in range(600):
        world.tick()

        if i % 20 == 0:
            print(f"\n---- Tick {i} | creatures: {len(world.creatures)} ----")
            print(world.render_ascii())
            time.sleep(0.1)


if __name__ == "__main__":
    main()
