from scale_player import ScalePlayer

player = ScalePlayer()
scale = player.generate_scale('g', 'mixolydian')
player.play_scale(scale, tempo=140, octave=4)