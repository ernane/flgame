import logging
import timeit

import numpy as np
import tensorflow as tf
from dynaconf import settings
from flask import Blueprint, current_app, jsonify, request

from flgame.ext.deep_learning.deep_reinforcement_learning import createNetwork

bp = Blueprint("api", __name__)

# Abrindo sessão
sess = tf.compat.v1.InteractiveSession()

# Previsões
x, prediction, _ = createNetwork()

# Carregando o modelo treinado
saver = tf.compat.v1.train.Saver()
checkpoint = tf.train.get_checkpoint_state(settings.MODEL_PATH)

if checkpoint and checkpoint.model_checkpoint_path:
    s = saver.restore(sess, checkpoint.model_checkpoint_path)
    logging.info(
        "Modelo carregado com sucesso: {}".format(checkpoint.model_checkpoint_path)
    )
else:
    logging.warning("Não foi possível carregar o modelo")
graph = tf.compat.v1.get_default_graph()


def bestmove(input):
    global graph
    logging.debug(graph.as_default())
    logging.debug(sess)
    starttime = timeit.default_timer()
    with graph.as_default():
        logging.debug(input)
        logging.debug("The start time is :{}".format(starttime))
        logging.debug(prediction)
        logging.debug(tf)
        data = sess.run(
            tf.argmax(prediction.eval(session=sess, feed_dict={x: [input]}), 1)
        )
        logging.debug("The time difference is :{}".format(timeit.default_timer() - starttime))
    logging.debug("bestmove Data => {}".format(data))
    return data


@bp.route("/api/ticky", methods=["POST"])
def ticky_api():
    current_app.logger.debug("Request => {}".format(request.get_json()))
    data = request.get_json()
    data = np.array(data["data"])
    data = data.tolist()
    current_app.logger.debug("Data => {}".format(data))
    return jsonify(np.asscalar(bestmove(data)[0]))
