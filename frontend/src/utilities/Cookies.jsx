import Cookies from "js-cookie";

export const setCookies = (name, value, days) => {
  try {
    return Cookies.set(name, value, { expires: days }) || true;
  } catch (err) {
    return console.error("Error setting cookie:", err) || false;
  }
};

export const getCookies = (name) => {
  try {
    return Cookies.get(name);
  } catch (err) {
    return console.error("Error getting cookie:", err) || false;
  }
};

export const removeCookies = (name) => {
  try {
    return Cookies.remove(name) || true;
  } catch (err) {
    return console.error("Error removing cookie:", err) || false;
  }
};
