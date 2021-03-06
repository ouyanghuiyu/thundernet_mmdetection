from torch.nn.modules.module import Module
from ..functions.psroi_align import PSRoIAlignFunction


class PSRoIAlign(Module):

    def __init__(self, out_size, spatial_scale, sample_num=0, output_dim=10, group_size=7):
        super(PSRoIAlign, self).__init__()

        self.out_size = out_size
        self.spatial_scale = float(spatial_scale)
        self.sample_num = int(sample_num)
        self.output_dim = int(output_dim)
        self.group_size = int(group_size)

    def forward(self, features, rois):
        return PSRoIAlignFunction.apply(features, rois, self.out_size,
                                      self.spatial_scale, self.sample_num,
                                      self.output_dim, self.group_size)
