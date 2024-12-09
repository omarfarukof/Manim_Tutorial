import manimlib as mgl
import numpy as np

class MakingSquare(mgl.Scene):
    def construct(self):
        self.add(mgl.ThreeDAxes())
        sq = mgl.VMobject()
        points = np.array([
            [-1,1,0],
            [-1,-1,0],
            [1,-1,0],
            [1,1,0]
        ])

        dots = mgl.VGroup(*[mgl.Dot(p) for p in points ])
        sq.set_points_as_corners(points)
        sq.add_points_as_corners( points[:1] )
        sq_sm = sq.copy()
        sq_sm.make_smooth()

        # self.add(dots)
        self.play(mgl.ShowCreation(dots) , run_time=2)

        self.play(mgl.ShowCreation(sq) , run_time=2)

        # sq_sm = sq.make_smooth()
        self.play(mgl.Transform(sq , sq_sm) , run_time=2)

        # self.clear()



