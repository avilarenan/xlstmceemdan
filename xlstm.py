import math
import torch as th
import torch.nn as nn

class LSTMCell(nn.Module):

    def __init__(self, input_size, hidden_size, bias=True):
        super(LSTM, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.bias = bias
        self.i2h = nn.Linear(input_size, 4 * hidden_size, bias=bias)
        self.h2h = nn.Linear(hidden_size, 4 * hidden_size, bias=bias)
        self.reset_parameters()

    def reset_parameters(self):
        std = 1.0 / math.sqrt(self.hidden_size)
        for w in self.parameters():
            w.data.uniform_(-std, std)

    def forward(self, x, hidden):

        if hidden is None:
            hidden = self._init_hidden(x)

        h, c = hidden
        h = h.view(h.size(1), -1)
        c = c.view(c.size(1), -1)
        x = x.view(x.size(1), -1)

        # Linear mappings
        preact = self.i2h(x) + self.h2h(h)

        # activations
        gates = preact[:, :3 * self.hidden_size].sigmoid()
        g_t = preact[:, 3 * self.hidden_size:].tanh()
        i_t = gates[:, :self.hidden_size]
        f_t = gates[:, self.hidden_size:2 * self.hidden_size]
        o_t = gates[:, -self.hidden_size:]

        c_t = th.mul(c, f_t) + th.mul(i_t, g_t)

        h_t = th.mul(o_t, c_t.tanh())

        h_t = h_t.view(1, h_t.size(0), -1)
        c_t = c_t.view(1, c_t.size(0), -1)
        return h_t, (h_t, c_t)

    @staticmethod
    def _init_hidden(input_):
        h = th.zeros_like(input_.view(1, input_.size(1), -1))
        c = th.zeros_like(input_.view(1, input_.size(1), -1))
        return h, c


class LSTM(nn.Module):

    def __init__(self, input_size, hidden_size, bias=True):
        super().__init__()
        self.lstm_cell = LSTMCell(input_size, hidden_size, bias)

    def forward(self, input_, hidden=None):
        # input_ is of dimensionalty (1, time, input_size, ...)

        outputs = []
        for x in torch.unbind(input_, dim=1):
            hidden = self.lstm_cell(x, hidden)
            outputs.append(hidden[0].clone())

        return torch.stack(outputs, dim=1)
