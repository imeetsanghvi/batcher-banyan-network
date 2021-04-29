from flask import Flask, render_template, request
import bbn

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template('input.html')
    else:
        results = request.form.to_dict()

        input_sequence = results.get('input_array').replace(" ", "")
        input_sequence = list(map(int, input_sequence.split(',')))

        temp = [k for k in input_sequence if -1 < k < 16]

        if not (len(temp) == len(input_sequence)):
            return render_template('input.html', method='POST', error='Enter Numbers in range 0 - 15 only or Comma '
                                                                      'separated values only ')

        # batcher implementation
        sorted_input_sequence = bbn.batcher_sorter(input_sequence)

        #  banyan implementation
        bbn.banyan_network(sorted_input_sequence)
        results = []
        for packet in sorted_input_sequence:
            results.append(str(packet.data).rjust(2) + "  --->  " + "  --->  ".join(packet.path))
            # results.append( [packet.data] + packet.path )
        return render_template('input.html', method='POST', results=results)


if __name__ == '__main__':
    app.run()
